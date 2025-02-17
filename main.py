import streamlit as st
import tempfile
from pathlib import Path
import os
from dotenv import load_dotenv
from DiagramKnowledgeBaseBuilder import DiagramKnowledgeBaseBuilder
from langchain_google_vertexai.model_garden import ChatAnthropicVertex
import json
import re
import uuid
from database import ConversationDB

# Load environment variables
load_dotenv()

# Initialize knowledge base
@st.cache_resource
def load_knowledge_base():
    kb = DiagramKnowledgeBaseBuilder()
    kb.load_knowledge_base('diagram_kb')
    return kb

def format_conversation_history():
    """Format the conversation history for the LLM"""
    conversation_history = ""
    for message in st.session_state["diagram_messages"]:
        if message[0] == "user":
            conversation_history += f"User: {message[1]}\n"
        else:
            # Only include text messages, not code or images
            if isinstance(message[1], str) and not message[1].startswith("Generated diagram code:"):
                conversation_history += f"Assistant: {message[1]}\n"
    return conversation_history

def generate_diagram_code(query: str, kb: DiagramKnowledgeBaseBuilder, error_msg: str = None, attempt: int = 1):
    """Generate diagram code using Claude and the knowledge base"""
    client = ChatAnthropicVertex(
        model="claude-3-5-sonnet-v2@20241022",
        temperature=0,
        max_output_tokens=2048,
        max_retries=6,
        top_p=0.8,
        top_k=40,
        verbose=True,
        location="us-east5"
    )
    
    # Get relevant examples from knowledge base
    results = kb.search(query, top_k=3)
    examples = [r for r in results if r[1]['type'] == 'example']
    providers = [r for r in results if r[1]['type'] == 'provider']
    
    # Format examples and providers for the prompt
    examples_text = "\n\n".join([
        f"Example {i+1}:\nQuestion: {ex[1]['question']}\nCode:\n{ex[1]['code']}"
        for i, ex in enumerate(examples)
    ])
    
    providers_text = "\n\n".join([
        f"Provider: {prov[1]['question']}\nComponents: {prov[1]['answer']}"
        for prov in providers
    ])
    
    system_prompt = """You are an expert in creating architecture diagrams using the Python diagrams library.
    Generate diagram code based on the user's requirements, using the provided examples and available components as reference.
    The code should be clear, well-structured, and follow best practices for the diagrams library.
    
    Important rules and syntax guidelines:
    1. Use only the components that are available in the provided components list
    2. Pay attention to exact component names (e.g., use 'Dynamodb' instead of 'DynamoDB')
    3. Include all necessary imports at the top of the file
    4. Set show=False in the Diagram constructor
    5. Use Cluster smart.
    6. Component connections must be between individual components, not lists:
       CORRECT:   component1 >> component2 >> component3
       INCORRECT: [component1, component2] >> [component3, component4]
    7. Each component must be instantiated separately:
       CORRECT:   
       comp1 = Component("label1")
       comp2 = Component("label2")
       comp1 >> comp2
       INCORRECT:
       [Component("label1"), Component("label2")] >> Component("label3")
    8. Always store components in variables before connecting them:
       CORRECT:
       db = Database("MyDB")
       app = Application("MyApp")
       db >> app
       INCORRECT:
       Database("MyDB") >> Application("MyApp")
    """
    
    error_context = f"\nPrevious error: {error_msg}\nPlease fix the error and ensure all components are available." if error_msg else ""
    
    response = client.invoke(
        f"""
        {system_prompt}
        
        User Request: {query}
        
        Available Examples:
        {examples_text}
        
        Available Components:
        {providers_text}
        {error_context}
        
        Generate Python code for a diagram that meets the user's requirements.
        Use only the components that are available in the diagrams library as shown in the Available Components section.
        The code should be complete and executable.
        Return only the Python code without any additional text or explanation.
        """
    )
    
    code = response.content
    
    try:
        # First attempt: Static code analysis
        if "[" in code and (">>" in code or "<<" in code):
            if attempt < 5:
                st.warning(f"Attempt {attempt}/5: Invalid list operation detected in component connections")
                return generate_diagram_code(query, kb, "Error: Cannot use list operations with components. Each component must be connected individually.", attempt + 1)
            return None

        # Second attempt: Check for direct component instantiation in connections
        connection_lines = [line.strip() for line in code.split('\n') if '>>' in line or '<<' in line]
        for line in connection_lines:
            if '(' in line and ')' in line and ('>>' in line or '<<' in line):
                if attempt < 5:
                    st.warning(f"Attempt {attempt}/5: Direct component instantiation in connections")
                    return generate_diagram_code(query, kb, "Error: Components must be stored in variables before connecting them.", attempt + 1)
                return None

        # Third attempt: Check for diagram initialization
        if "with Diagram(" not in code:
            if attempt < 5:
                st.warning(f"Attempt {attempt}/5: Missing Diagram initialization")
                return generate_diagram_code(query, kb, "Error: Missing Diagram initialization", attempt + 1)
            return None

        # Fourth attempt: Validate component connections
        if ">> " not in code and " << " not in code:
            if attempt < 5:
                st.warning(f"Attempt {attempt}/5: No component connections found")
                return generate_diagram_code(query, kb, "Error: No component connections defined", attempt + 1)
            return None

        # Fifth attempt: Test code execution
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_file = Path(tmpdir) / "test_code.py"
            with open(temp_file, "w") as f:
                f.write(code)
            try:
                exec(code)
            except Exception as e:
                error_msg = str(e)
                if "unsupported operand type(s) for >>" in error_msg:
                    error_msg = "Components must be connected individually, not as lists. Use separate variables for each component."
                if attempt < 5:
                    st.warning(f"Attempt {attempt}/5: Runtime error - {error_msg}")
                    return generate_diagram_code(query, kb, f"Runtime error: {error_msg}", attempt + 1)
                return None

        return code
    except Exception as e:
        if attempt < 5:
            st.warning(f"Attempt {attempt}/5: Unexpected error - {str(e)}")
            return generate_diagram_code(query, kb, f"Unexpected error: {str(e)}", attempt + 1)
        return None

def render_diagram(code: str):
    """Execute the diagram code and return the generated image"""
    if not code:
        return None
        
    # Create a temporary directory for the diagram
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write the code to a temporary file
        temp_file = Path(tmpdir) / "diagram_code.py"
        with open(temp_file, "w") as f:
            f.write(code)
        
        # Execute the code to generate the diagram
        current_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            exec(code)
            # Find the generated diagram file
            for file in Path(tmpdir).glob("*.png"):
                return file.read_bytes()
        except Exception as e:
            st.error(f"Error generating diagram: {str(e)}")
            return None
        finally:
            os.chdir(current_dir)

def generate_summary(query: str, code: str):
    """Generate a summary of the architecture using Claude"""
    client = ChatAnthropicVertex(
        model="claude-3-5-sonnet-v2@20241022",
        temperature=0,
        max_output_tokens=1024,
        max_retries=6,
        top_p=0.8,
        top_k=40,
        verbose=True,
        location="us-east5"
    )
    
    response = client.invoke(
        f"""
        You are an expert in explaining software architecture. Provide a clear, concise summary of this architecture diagram.
        
        User Request: {query}
        
        Diagram Code:
        {code}
        
        Provide a brief summary of this architecture, explaining the key components and their relationships.
        Focus on the high-level design decisions and how they address the requirements.
        """
    )
    
    return response.content

# Initialize session state and database
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if "diagram_messages" not in st.session_state:
    # Initialize database connection
    db = ConversationDB()
    # Load existing messages for this session
    st.session_state["diagram_messages"] = db.get_session_messages(st.session_state["session_id"])
    # Clean up old sessions
    db.clear_old_sessions()

# Streamlit UI
st.title("Architecture Diagram Generator")
st.write("Describe your architecture requirements, and I'll help you create a diagram using the Python diagrams library.")

# User input
query = st.text_area("Describe your architecture:", height=100)

if st.button("Generate Diagram"):
    if query:
        # Add user message to history and database
        db = ConversationDB()
        st.session_state["diagram_messages"].append(("user", query))
        db.add_message("user", query, st.session_state["session_id"])
        
        # Load knowledge base
        kb = load_knowledge_base()
        
        # Generate diagram code with retries
        with st.spinner("Generating diagram code..."):
            code = generate_diagram_code(query, kb)
            if code:
                st.session_state["diagram_messages"].append(("assistant", "Generated diagram code:"))
                st.code(code, language="python")
                
                # Render diagram
                with st.spinner("Rendering diagram..."):
                    diagram_image = render_diagram(code)
                    if diagram_image:
                        st.image(diagram_image, caption="Generated Architecture Diagram")
                        
                        # Generate and show summary
                        with st.spinner("Generating summary..."):
                            summary = generate_summary(query, code)
                            st.session_state["diagram_messages"].append(("assistant", summary))
                            db = ConversationDB()
                            db.add_message("assistant", summary, st.session_state["session_id"])
                            st.markdown("### Summary")
                            st.write(summary)
                            
                        # Show similar examples
                        if len(st.session_state["diagram_messages"]) > 1:
                            with st.expander("Similar Examples"):
                                results = kb.search(query, top_k=3)
                                examples = [r for r in results if r[1]['type'] == 'example']
                                for score, example in examples[1:]:
                                    st.markdown(f"**Similarity Score:** {score:.2f}")
                                    st.markdown(f"**Use Case:** {example['question']}")
                                    st.markdown(f"**Description:** {example['answer']}")
                                    st.code(example['code'], language="python")
            else:
                st.error("Could not generate valid diagram code. Please try a different description.")
    else:
        st.warning("Please enter your architecture requirements.")

# Display conversation history
# st.sidebar.markdown("### Conversation History")
# for role, message in st.session_state["diagram_messages"]:
#     # Create unique key using index and role
#     message_idx = st.session_state["diagram_messages"].index((role, message))
#     if role == "user":
#         st.sidebar.text_area("User:", message, height=100, disabled=True, key=f"user_message_{message_idx}")
#     else:
#         st.sidebar.text_area("Assistant:", message, height=100, disabled=True, key=f"assistant_message_{message_idx}")
