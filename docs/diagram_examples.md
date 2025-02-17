# Diagram Usage Examples

## AWS Examples

### Containers


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


### Serverless


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


## AZURE Examples

### Microservices


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


## GCP Examples

### Ml_Pipeline


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


## PATTERNS Examples

### Clustered_Services


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


### Custom_Broker


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


### Event_Processing


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


### Load_Balanced


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


### Stateful_K8S


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

