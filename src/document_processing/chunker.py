from abc import ABC, abstractmethod

class DocumentChunker(ABC):
    @abstractmethod
    def chunk(self, text, chunk_size):
        pass

class SimpleChunker(DocumentChunker):
    def chunk(self, text, chunk_size=1000):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

class ChunkerFactory:
    @staticmethod
    def get_chunker(chunker_type='simple'):
        if chunker_type == 'simple':
            return SimpleChunker()
        # Add more chunkers in the future
        raise ValueError(f"Unsupported chunker type: {chunker_type}")