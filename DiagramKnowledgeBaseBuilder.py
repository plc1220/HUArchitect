import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Tuple
import re

class DiagramKnowledgeBaseBuilder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """Initialize the knowledge base builder with a sentence transformer model."""
        self.model = SentenceTransformer(model_name)
        self.examples: List[Dict] = []
        self.embeddings: np.ndarray = None
        
    def extract_knowledge_base(self, examples_path: str, providers_path: str, docs_path: str = None) -> List[Dict]:
        """Extract knowledge from markdown files into a unified knowledge base.
        
        Args:
            examples_path: Path to examples markdown file (like Correct Answers)
            providers_path: Path to providers markdown file (like DDL/Schemas) 
            docs_path: Optional path to documentation markdown file (like Documentation)
        """
        self.entries = []
        
        # Process provider definitions (like DDL/Schemas)
        print(f"Reading providers file: {providers_path}")
        providers_content = Path(providers_path).read_text()
        self._extract_provider_definitions(providers_content)
        
        # Process examples (like Correct Answers)
        print(f"Reading examples file: {examples_path}")
        examples_content = Path(examples_path).read_text()
        self._extract_examples(examples_content)
        
        # Process documentation if provided
        if docs_path:
            print(f"Reading documentation file: {docs_path}")
            docs_content = Path(docs_path).read_text()
            self._extract_documentation(docs_content)
            
        return self.entries
        
    def _extract_provider_definitions(self, content: str):
        """Extract provider component definitions and relationships (like DDL/Schemas)."""
        sections = content.split('\n# ')
        for section in sections:
            if not section.strip():
                continue
                
            lines = section.strip().split('\n')
            if not lines:
                continue
                
            provider = lines[0].strip().replace('# ', '').lower()
            current_category = None
            
            for line in lines[1:]:
                if line.startswith('## '):
                    # New category section
                    current_category = line.replace('## ', '').strip()
                elif line.startswith('- ') and current_category:
                    # Component definition
                    comp_parts = line.replace('- ', '').split(': ', 1)
                    if len(comp_parts) == 2:
                        comp_name = comp_parts[0].strip()
                        description = comp_parts[1].strip()
                        
                        # Add component with rich metadata
                        entry = {
                            'type': 'component',
                            'provider': provider,
                            'component': comp_name,
                            'category': current_category,
                            'module': f"diagrams.{provider}.{current_category.lower()}",
                            'description': description,
                            'search_text': f"{provider} {current_category} {comp_name} {description}"
                        }
                        self.entries.append(entry)
                        
            print(f"Found provider: {provider} with components")
            
    def _extract_examples(self, content: str):
        """Extract example diagrams and their descriptions (like Correct Answers)."""
        sections = content.split('\n### ')
        for section in sections:
            if not section.strip():
                continue
                
            # Find Q&A pairs
            q_parts = section.split('\nQ: ')
            if len(q_parts) < 2:
                continue
                
            q_content = q_parts[1]
            a_parts = q_content.split('\nA: ')
            if len(a_parts) < 2:
                continue
                
            question = a_parts[0].strip()
            remaining = a_parts[1]
            
            # Find code block
            code_parts = remaining.split('```python\n')
            if len(code_parts) < 2:
                continue
                
            answer = code_parts[0].split('\n\nDiagram:')[0].strip()
            code = code_parts[1].split('\n```')[0].strip()
            
            # Add example with rich metadata
            entry = {
                'type': 'example',
                'question': question,
                'answer': answer,
                'code': code,
                'search_text': f"{question} {answer}"
            }
            print(f"Found example: {entry['question'][:50]}...")
            self.entries.append(entry)
            
    def _extract_documentation(self, content: str):
        """Extract documentation and best practices (like Documentation)."""
        sections = content.split('\n## ')
        for section in sections:
            if not section.strip():
                continue
                
            lines = section.strip().split('\n')
            if not lines:
                continue
                
            title = lines[0].strip()
            content = '\n'.join(lines[1:]).strip()
            
            # Add documentation with metadata
            entry = {
                'type': 'documentation',
                'title': title,
                'content': content,
                'search_text': f"{title} {content}"
            }
            print(f"Found documentation: {entry['title']}")
            self.entries.append(entry)
    
    def build_embeddings(self):
        """Create embeddings for all knowledge base entries."""
        if not self.entries:
            raise ValueError("No entries loaded. Call extract_knowledge_base first.")
            
        # Construct search text based on entry type
        texts = []
        for entry in self.entries:
            if entry['type'] == 'example':
                search_text = f"{entry['question']} {entry['answer']}"
            elif entry['type'] == 'provider' or entry['type'] == 'component':
                search_text = f"{entry['provider']} {entry['component']} {entry['module']} {entry['description']}"
            else:
                search_text = str(entry)  # Fallback for unknown types
            texts.append(search_text)
        
        # Create embeddings
        self.embeddings = self.model.encode(texts, convert_to_tensor=True)
        
    def save_knowledge_base(self, output_dir: str):
        """Save the unified knowledge base and embeddings."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save knowledge base entries
        with open(output_path / 'knowledge_base.json', 'w') as f:
            json.dump(self.entries, f, indent=2)
            
        # Save embeddings
        np.save(output_path / 'embeddings.npy', self.embeddings.cpu().numpy())
        
    def load_knowledge_base(self, input_dir: str):
        """Load a saved knowledge base and embeddings."""
        input_path = Path(input_dir)
        
        # Load knowledge base entries
        with open(input_path / 'knowledge_base.json', 'r') as f:
            self.entries = json.load(f)
            
        # Load embeddings
        self.embeddings = np.load(input_path / 'embeddings.npy')
        
    def search(self, query: str, top_k: int = 3, entry_type: str = None) -> List[Tuple[float, Dict]]:
        """Search for most relevant entries given a query.
        
        Args:
            query: The search query
            top_k: Number of results to return
            entry_type: Optional filter for entry type ('component', 'example', 'documentation')
        """
        if self.embeddings is None:
            raise ValueError("No embeddings available. Build or load knowledge base first.")
            
        # Create embedding for query
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        
        # Calculate cosine similarities
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Filter by type if specified
        if entry_type:
            # Handle both 'provider' and 'component' types
            if entry_type == 'component':
                type_indices = [i for i, entry in enumerate(self.entries) if entry['type'] in ('provider', 'component')]
            else:
                type_indices = [i for i, entry in enumerate(self.entries) if entry['type'] == entry_type]
            similarities = similarities[type_indices]
            entries = [self.entries[i] for i in type_indices]
        else:
            entries = self.entries
        
        # Get top k matches
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        return [(similarities[i], entries[i]) for i in top_indices]

def main():
    """Example usage of the unified knowledge base."""
    kb_builder = DiagramKnowledgeBaseBuilder()
    
    # Extract knowledge from markdown files
    kb_builder.extract_knowledge_base(
        examples_path='docs/diagram_examples.md',
        providers_path='docs/diagram_providers.md',
        docs_path='docs/diagram_docs.md'
    )
    
    # Build embeddings
    kb_builder.build_embeddings()
    
    # Save knowledge base
    kb_builder.save_knowledge_base('diagram_kb')
    
    # Example searches
    print("\nSearching for examples:")
    results = kb_builder.search("How to create a serverless API?", entry_type='example')
    print_results(results)
    
    print("\nSearching for components:")
    results = kb_builder.search("AWS database components", entry_type='component')
    print_results(results)
    
    print("\nSearching all types:")
    results = kb_builder.search("event driven architecture")  # No type filter
    print_results(results)

def print_results(results):
    """Print search results based on entry type."""
    print("\nSearch Results:")
    for score, entry in results:
        print(f"\nScore: {score:.3f}")
        print(f"Type: {entry['type']}")
        
        if entry['type'] == 'example':
            print(f"Question: {entry['question']}")
            print(f"Answer: {entry['answer']}")
            print("Code:")
            print(entry['code'])
        elif entry['type'] == 'component':
            print(f"Provider: {entry['provider'].upper()}")
            print(f"Component: {entry['component']}")
            print(f"Category: {entry['category']}")
            print(f"Description: {entry['description']}")
        else:  # documentation
            print(f"Title: {entry['title']}")
            print(f"Content: {entry['content'][:200]}...")

if __name__ == "__main__":
    main()
