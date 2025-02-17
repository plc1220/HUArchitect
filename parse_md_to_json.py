import re
import json

def parse_examples_md(content):
    examples = []
    sections = content.split('\n## ')[1:]  # Split by level 2 headers, skip first empty part
    
    for section in sections:
        # Split section into subsections
        subsections = section.split('\n### ')[1:]  # Skip section title
        
        for subsection in subsections:
            # Extract Q&A and code blocks
            lines = subsection.strip().split('\n')
            
            # Find question and answer
            q_match = next((line for line in lines if line.startswith('Q: ')), None)
            a_match = next((line for line in lines if line.startswith('A: ')), None)
            
            if q_match and a_match:
                question = q_match[3:].strip()
                answer = a_match[3:].strip()
                
                # Find code block
                code_start = subsection.find('```python')
                code_end = subsection.find('```', code_start + 8)
                if code_start != -1 and code_end != -1:
                    code = subsection[code_start + 8:code_end].strip()
                    
                    examples.append({
                        "type": "example",
                        "question": question,
                        "answer": answer,
                        "code": code
                    })
    
    return examples

def parse_providers_md(content):
    providers = []
    current_provider = None
    
    # Split content into lines and process each line
    for line in content.split('\n'):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check for provider header
        if line.startswith('# '):
            current_provider = line[2:].lower()
            continue
            
        # Process import lines
        if line.startswith('from diagrams.'):
            # Extract module path and components
            parts = line.split(' import ')
            if len(parts) != 2:
                continue
                
            module_path = parts[0].replace('from ', '')
            components = [c.strip() for c in parts[1].split(',')]
            
            # Add each component
            for component in components:
                if component:  # Skip empty components
                    providers.append({
                        "type": "provider",
                        "provider": current_provider,
                        "component": component,
                        "module": module_path,
                        "description": f"{component} is a {current_provider.upper()} {module_path.split('.')[-1]} component"
                    })
    
    return providers

def main():
    # Read examples markdown
    with open('docs/diagram_examples.md', 'r') as f:
        examples_content = f.read()
    
    # Read providers markdown
    with open('docs/diagram_providers.md', 'r') as f:
        providers_content = f.read()
    
    # Parse both files
    examples = parse_examples_md(examples_content)
    providers = parse_providers_md(providers_content)
    
    # Combine results
    combined = examples + providers
    
    # Write to JSON file
    with open('example.json', 'w') as f:
        json.dump(combined, f, indent=2)

if __name__ == "__main__":
    main()
