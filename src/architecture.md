##TO BE UPDATED
## Component Responsibilities

### document_loader.py

- Defines the `DocumentLoader` abstract base class.
- Implements `TxtLoader` for loading text files.
- Contains `LoaderFactory` for creating appropriate loader instances.

Responsibilities:
- Provide a consistent interface for loading different types of documents.
- Read the content of documents from file system.

### text_processor.py

- Defines the `TextProcessor` abstract base class.
- Implements `BasicTextProcessor` for basic text cleaning and normalization.
- Contains `ProcessorFactory` for creating processor instances.

Responsibilities:
- Clean and normalize text content.
- Remove special characters, normalize whitespace, and convert text to lowercase.

### document_chunker.py

- Defines the `DocumentChunker` abstract base class.
- Implements `SimpleChunker` for basic text chunking.
- Contains `ChunkerFactory` for creating chunker instances.

Responsibilities:
- Split processed text into manageable chunks for further processing or embedding.

### document_collector.py

- Implements `DocumentCollector` class.

Responsibilities:
- Scan a specified directory for document files.
- Collect file paths and names of documents to be processed.

### processing_pipeline.py

- Implements `ProcessingPipeline` class.

Responsibilities:
- Orchestrate the document processing workflow.
- Combine loading, processing, and chunking operations.

### document_manager.py

- Defines `DocumentMetadata` dataclass.
- Implements `DocumentManager` class.

Responsibilities:
- Store and manage processed documents and their metadata.
- Provide an interface for adding and retrieving processed documents.

### main.py

- Contains the main execution logic of the RAG system.

Responsibilities:
- Initialize and coordinate all components of the system.
- Execute the document ingestion and processing workflow.
- Demonstrate the output of the processing pipeline.

## Workflow

1. `DocumentCollector` scans the `documents/` directory for files.
2. For each document:
   a. `DocumentLoader` reads the file content.
   b. `TextProcessor` cleans and normalizes the text.
   c. `DocumentChunker` splits the processed text into chunks.
3. `ProcessingPipeline` orchestrates these steps.
4. `DocumentManager` stores the processed chunks along with metadata.