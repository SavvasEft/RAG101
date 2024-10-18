import os
from src.document_processing import DocumentCollector, ProcessingPipeline
from src.document_processing.loader import LoaderFactory
from src.document_processing.processor import ProcessorFactory
from src.document_processing.chunker import ChunkerFactory
from src.database.document_manager import DocumentManager

def main():
    manager = DocumentManager()
    collector = DocumentCollector('documents')
    loader = LoaderFactory.get_loader('txt')
    processor = ProcessorFactory.get_processor()
    chunker = ChunkerFactory.get_chunker()
    pipeline = ProcessingPipeline(loader, processor, chunker)

    
    # Ask for confirmation before resetting
    # confirm = input("Are you sure you want to reset the database? This will delete all data. (y/n): ")
    # if confirm.lower() == 'y':
    #     manager.reset_database()
    #     print("Database has been reset.")
    # else:
    #     print("Database reset cancelled.")
        
        
    for filename, path in collector.collect():
        if not manager.document_exists(filename, path) or \
           os.path.getmtime(path) > manager.get_document(filename, path)['processed_date'].timestamp():
            chunks = pipeline.process(path)
            manager.update_document(filename, path, chunks)

    # Print results
    for doc in manager.get_all_documents():
        print(f"File: {doc['filename']}")
        print(f"Path: {doc['path']}")
        print(f"Processed Date: {doc['processed_date']}")
        print(f"Number of chunks: {doc['chunk_count']}")
        print(f"First chunk: {doc['chunks'][0][:100]}...")  # Assuming chunks are stored as strings
        print()

    manager.close()

if __name__ == "__main__":
    main()