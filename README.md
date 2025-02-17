# Architecture Diagram Generator

A Streamlit application that helps generate architecture diagrams using the Python diagrams library. The app is inspired by Vanna's approach of retrieving context before generating diagrams.

## Features

- Interactive diagram generation through natural language descriptions
- Knowledge base of cloud provider components and example diagrams
- Semantic search for finding relevant components and examples
- Integration with Claude for intelligent diagram analysis and generation
- Live diagram rendering and code preview
- Conversation history tracking

## Project Structure

```
.
├── main.py                         # Streamlit application
├── DiagramKnowledgeBaseBuilder.py  # Knowledge base management
├── test_kb.py                      # Knowledge base testing
├── rebuild_kb.py                   # Knowledge base rebuilding utility
├── diagram_kb/                     # Knowledge base data
│   ├── embeddings.npy             # Sentence embeddings
│   ├── examples.json              # Example diagrams
│   └── knowledge_base.json        # Unified knowledge base
└── docs/                          # Documentation
    ├── diagram_examples.md        # Example diagrams
    └── diagram_providers.md       # Provider components
```

## Setup

1. Create a virtual environment:
```bash
python -m venv CA
source CA/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install streamlit diagrams sentence-transformers langchain-google-vertexai python-dotenv
```

3. Set up environment variables in `.env`:
```
OPENWEATHER_API_KEY=your_api_key
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Enter your architecture requirements in the text area
3. Click "Generate Diagram" to create the diagram
4. Review the generated diagram, code, and summary
5. Use the conversation history to refine the diagram

## Knowledge Base

The system uses a knowledge base that contains:
- Cloud provider components (AWS, Azure, GCP, etc.)
- Example architecture diagrams with code
- Best practices and documentation

The knowledge base can be rebuilt using:
```bash
python rebuild_kb.py
```

Test the knowledge base retrieval with:
```bash
python test_kb.py
```

## How It Works

1. User provides architecture requirements
2. System analyzes requirements using Claude
3. Relevant components and examples are retrieved from knowledge base
4. Diagram code is generated based on requirements and examples
5. Code is executed to render the diagram
6. Summary is generated to explain the architecture

## Example Usage

```python
# Example: Create a serverless API
from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamoDB
from diagrams.aws.network import APIGateway

with Diagram("Serverless API", show=False):
    api = APIGateway("API Gateway")
    lambda_fn = Lambda("API Handler")
    db = DynamoDB("Users Table")
    
    api >> lambda_fn >> db
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
