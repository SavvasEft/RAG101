import re
from abc import ABC, abstractmethod

class TextProcessor(ABC):
    @abstractmethod
    def process(self, text):
        pass

class BasicTextProcessor(TextProcessor):
    def process(self, text):
        # Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text.lower()

class ProcessorFactory:
    @staticmethod
    def get_processor(processor_type='basic'):
        if processor_type == 'basic':
            return BasicTextProcessor()
        # Add more processors in the future
        raise ValueError(f"Unsupported processor type: {processor_type}")