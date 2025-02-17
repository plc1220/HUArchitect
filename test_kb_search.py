from DiagramKnowledgeBaseBuilder import DiagramKnowledgeBaseBuilder

kb = DiagramKnowledgeBaseBuilder()

kb.load_knowledge_base('diagram_kb')

# Test example retrieval
print("\n=== Testing Example Retrieval ===")
example_queries = [
    "serverless event driven architecture with GCP",
    "microservices architecture with containers",
    "data pipeline with streaming"
]

for query in example_queries:
    print(f"\nQuery: {query}")
    results = kb.search(query, top_k=2, entry_type='example')
    for score, entry in results:
        print(f"Score: {score}")
        print(f"Question: {entry['question']}")
        print(f"Code snippet:\n{entry['code'][:500]}...")

# Test component retrieval
print("\n=== Testing Component Retrieval ===")
component_queries = [
    "GCP compute components",
    "AWS Lambda compute serverless",
    "AWS EventBridge integration serverless",
    "AWS DynamoDB database serverless"
]

for query in component_queries:
    print(f"\nQuery: {query}")
    results = kb.search(query, top_k=2, entry_type='component')
    for score, entry in results:
        print(f"Score: {score}")
        print(f"Provider: {entry['provider'].upper()}")
        print(f"Component: {entry['component']}")
        print(f"Module: {entry['module']}")
        print(f"Description: {entry['description']}")

# Test mixed retrieval
print("\n=== Testing Mixed Retrieval ===")
mixed_queries = [
    "event driven architecture",
    "serverless components and examples",
    "database options"
]

for query in mixed_queries:
    print(f"\nQuery: {query}")
    results = kb.search(query, top_k=3)  # No type filter
    for score, entry in results:
        print(f"Score: {score}")
        print(f"Type: {entry['type']}")
        if entry['type'] == 'example':
            print(f"Question: {entry['question']}")
        elif entry['type'] in ('provider', 'component'):
            print(f"Provider: {entry['provider'].upper()}")
            print(f"Component: {entry['component']}")
            print(f"Module: {entry['module']}")
            print(f"Description: {entry['description']}")
        else:  # documentation
            print(f"Title: {entry['title']}")
