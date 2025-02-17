import inspect
import importlib
import pkgutil
import diagrams
from pathlib import Path
import textwrap

class DiagramsDocGenerator:
    def __init__(self):
        self.providers_path = Path(diagrams.__file__).parent
        self.output_path = Path("docs/diagram_providers.md")
        self.excluded_modules = {'_template', '__pycache__', '__init__'}

    def get_provider_modules(self):
        """Get all provider modules from diagrams library"""
        providers = {}
        
        # Walk through all modules in diagrams package
        for _, name, _ in pkgutil.iter_modules([str(self.providers_path)]):
            if name not in self.excluded_modules:
                providers[name] = []
                provider_path = self.providers_path / name
                
                # Get all service modules for each provider
                if provider_path.is_dir():
                    for _, service_name, _ in pkgutil.iter_modules([str(provider_path)]):
                        if service_name not in self.excluded_modules:
                            providers[name].append(service_name)
                            
        return providers

    def get_module_resources(self, provider: str, service: str) -> list:
        """Get all resource classes from a specific module"""
        try:
            module = importlib.import_module(f"diagrams.{provider}.{service}")
            resources = []
            
            for name, obj in inspect.getmembers(module):
                # Get only classes that are defined in this module
                if (inspect.isclass(obj) and 
                    obj.__module__ == f"diagrams.{provider}.{service}" and
                    not name.startswith('_')):
                    resources.append(name)
                    
            return sorted(resources)
        except ImportError as e:
            print(f"Warning: Could not import diagrams.{provider}.{service}: {e}")
            return []

    def generate_markdown(self):
        """Generate markdown documentation for all providers"""
        providers = self.get_provider_modules()
        markdown_content = []
        
        for provider, services in sorted(providers.items()):
            # Add provider section
            markdown_content.append(f"# {provider.upper()}")
            
            for service in sorted(services):
                resources = self.get_module_resources(provider, service)
                if resources:
                    # Create import statement
                    import_stmt = f"from diagrams.{provider}.{service} import {', '.join(resources)}"
                    # Wrap long lines
                    wrapped_import = textwrap.fill(import_stmt, width=100, 
                                                 subsequent_indent='    ')
                    markdown_content.append(wrapped_import)
            
            markdown_content.append("")  # Add blank line between providers
        
        # Write to file
        self.output_path.parent.mkdir(exist_ok=True)
        self.output_path.write_text('\n'.join(markdown_content))
        print(f"Generated providers documentation at {self.output_path}")

    def get_usage_examples(self) -> dict:
        """Get example usages of different node types"""
        examples = {
            'aws': {
                'serverless': """
Q: Create a serverless API with AWS Lambda and DynamoDB
A: This architecture demonstrates a basic serverless API setup using AWS Lambda for request handling and DynamoDB for data storage.

Diagram:
```python
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
""",
                'containers': """
Q: Design a containerized application architecture with ECS
A: This architecture shows a containerized application running on Amazon ECS with load balancing and RDS database.

Diagram:
```python
from diagrams import Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Containerized App", show=False):
    lb = ELB("Load Balancer")
    containers = [ECS("Container 1"),
                 ECS("Container 2")]
    db = RDS("Database")
    
    lb >> containers >> db
```
"""
            },
            'azure': {
                'microservices': """
Q: Create a microservices architecture using Azure Kubernetes Service
A: This architecture demonstrates a microservices setup using AKS with Azure SQL Database for persistence.

Diagram:
```python
from diagrams import Diagram
from diagrams.azure.compute import AKS
from diagrams.azure.database import SQLDatabases
from diagrams.azure.network import LoadBalancers

with Diagram("Azure Microservices", show=False):
    lb = LoadBalancers("Load Balancer")
    aks = AKS("Kubernetes")
    db = SQLDatabases("Azure SQL")
    
    lb >> aks >> db
```
"""
            },
            'gcp': {
                'ml_pipeline': """
Q: Design a machine learning pipeline on Google Cloud
A: This architecture shows a machine learning pipeline using various GCP services for data processing and model training.

Diagram:
```python
from diagrams import Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.gcp.ml import AIPlatform

with Diagram("ML Pipeline", show=False):
    bq = BigQuery("Data Warehouse")
    flow = Dataflow("Data Processing")
    ml = AIPlatform("Model Training")
    
    bq >> flow >> ml
```
"""
            },
            'patterns': {
                'load_balanced': """
Q: How to represent a load-balanced worker pool architecture?
A: This example shows multiple EC2 workers behind a load balancer writing to a central database.

Diagram:
```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")
```
""",
                'clustered_services': """
Q: How to design a clustered web services architecture with caching?
A: This example demonstrates a clustered web service setup with DNS, load balancing, multiple web servers, database replication, and caching.

Diagram:
```python
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
```
""",
                'event_processing': """
Q: How to implement an event processing architecture?
A: This example shows a complex event processing system with Kubernetes source, worker clusters, queues, and multiple processing handlers.

Diagram:
```python
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=False):
    source = EKS("k8s source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        queue = SQS("event queue")

        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]

    store = S3("events store")
    dw = Redshift("analytics")

    source >> workers >> queue >> handlers
    handlers >> store
    handlers >> dw
```
""",
                'stateful_k8s': """
Q: How to diagram a stateful Kubernetes architecture?
A: This example shows a stateful application in Kubernetes with persistent volumes and storage classes.

Diagram:
```python
from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service
from diagrams.k8s.storage import PV, PVC, StorageClass

with Diagram("Stateful Architecture", show=False):
    with Cluster("Apps"):
        svc = Service("svc")
        sts = StatefulSet("sts")

        apps = []
        for _ in range(3):
            pod = Pod("pod")
            pvc = PVC("pvc")
            pod - sts - pvc
            apps.append(svc >> pod >> pvc)

    apps << PV("pv") << StorageClass("sc")
```
""",
                'custom_broker': """
Q: How to create diagrams with custom icons and message brokers?
A: This example demonstrates using custom icons and showing a message broker architecture with Kubernetes consumers.

Diagram:
```python
from urllib.request import urlretrieve

from diagrams import Cluster, Diagram
from diagrams.aws.database import Aurora
from diagrams.custom import Custom
from diagrams.k8s.compute import Pod

# Download an image to be used into a Custom Node class
rabbitmq_url = "https://jpadilla.github.io/rabbitmqapp/assets/img/icon.png"
rabbitmq_icon = "rabbitmq.png"
urlretrieve(rabbitmq_url, rabbitmq_icon)

with Diagram("Broker Consumers", show=False):
    with Cluster("Consumers"):
        consumers = [
            Pod("worker"),
            Pod("worker"),
            Pod("worker")]

    queue = Custom("Message queue", rabbitmq_icon)

    queue >> consumers >> Aurora("Database")
```
"""
            }
        }
        return examples

    def generate_examples_doc(self):
        """Generate markdown documentation for usage examples"""
        examples = self.get_usage_examples()
        markdown_content = ["# Diagram Usage Examples\n"]
        
        for provider, categories in sorted(examples.items()):
            markdown_content.append(f"## {provider.upper()} Examples\n")
            
            for category, example in sorted(categories.items()):
                markdown_content.append(f"### {category.title()}\n")
                markdown_content.append(example)
                markdown_content.append("")  # Add blank line
        
        # Write to examples file
        examples_path = self.output_path.parent / "diagram_examples.md"
        examples_path.write_text('\n'.join(markdown_content))
        print(f"Generated examples documentation at {examples_path}")

    def generate_full_documentation(self):
        """Generate complete documentation including providers and examples"""
        try:
            # Create docs directory if it doesn't exist
            self.output_path.parent.mkdir(exist_ok=True)
            
            # Generate providers documentation
            self.generate_markdown()
            
            # Generate examples documentation
            self.generate_examples_doc()
            
            # Generate index file
            index_content = [
                "# Diagrams Library Documentation\n",
                "This documentation provides a comprehensive guide to using the diagrams library.\n",
                "## Contents\n",
                "1. [Providers Reference](diagram_providers.md)",
                "2. [Usage Examples](diagram_examples.md)\n",
                "## Quick Start\n",
                "```python",
                "from diagrams import Diagram",
                "from diagrams.aws.compute import EC2",
                "from diagrams.aws.database import RDS\n",
                "with Diagram('Simple Web Service', show=False):",
                "    web = EC2('Web Server')",
                "    db = RDS('Database')",
                "    web >> db",
                "```"
            ]
            
            index_path = self.output_path.parent / "index.md"
            index_path.write_text('\n'.join(index_content))
            print(f"Generated index documentation at {index_path}")
            
        except Exception as e:
            print(f"Error generating documentation: {str(e)}")
            raise


if __name__ == "__main__":
    try:
        doc_generator = DiagramsDocGenerator()
        doc_generator.generate_full_documentation()
        print("Documentation generation completed successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)
