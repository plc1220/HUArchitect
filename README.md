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

### Local Setup

1. Create a virtual environment:
```bash
python -m venv CA
source CA/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Docker Setup

1. Build and run using Docker Compose:
```bash
docker-compose up --build
```

This will start both the application and the PostgreSQL database.

## Environment Configuration

Create a `.env` file based on `.env.example`:

```
# Database Configuration
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_NAME=diagram_db
DB_HOST=db
DB_PORT=5432

# Google Vertex AI Configuration
GOOGLE_APPLICATION_CREDENTIALS=/app/my-rd-coe-demo-data-0f2a5a8dbc36.json
VERTEX_AI_PROJECT=your_project_id
VERTEX_AI_LOCATION=us-east5

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## Usage

1. Start the application:
   - Local: `streamlit run main.py`
   - Docker: `docker-compose up`
2. Enter your architecture requirements in the text area
3. Click "Generate Diagram" to create the diagram
4. Review the generated diagram, code, and summary
5. Use the conversation history to refine the diagram

## Example Architecture Diagrams

The project includes several example architecture diagrams:

- `3-tier_architecture.png` - Basic three-tier application architecture
- `3-tier_auto_scaling_app.png` - Three-tier architecture with auto-scaling
- `airflow_on_eks_architecture.png` - Apache Airflow deployment on EKS
- `aws_3-tier_architecture.png` - AWS-specific three-tier architecture
- `azure_ml_pipeline.png` - Azure Machine Learning pipeline
- `gcp_batch_analytics.png` - GCP batch analytics architecture
- `gcp_data_analytics.png` - GCP data analytics pipeline
- `mern_stack_on_eks.png` - MERN stack deployment on EKS
- `netflix_clone_architecture.png` - Netflix-like streaming service architecture
- `serverless_api.png` - Serverless API architecture
- `whatsapp_clone_on_gcp.png` - WhatsApp-like messaging service on GCP

These examples serve as references and can be used as templates for generating similar architectures.

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
