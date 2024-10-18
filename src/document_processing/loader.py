import os
from abc import ABC, abstractmethod

class DocumentLoader(ABC):
    @abstractmethod
    def load(self, path):
        pass

class TxtLoader(DocumentLoader):
    def load(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

class LoaderFactory:
    @staticmethod
    def get_loader(file_type):
        if file_type == 'txt':
            return TxtLoader()
        # Add more loaders for different file types in the future
        raise ValueError(f"Unsupported file type: {file_type}")

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_type = filename.split('.')[-1].lower()
        loader = LoaderFactory.get_loader(file_type)
        full_path = os.path.join(folder_path, filename)
        documents.append((filename, loader.load(full_path)))
    return documents