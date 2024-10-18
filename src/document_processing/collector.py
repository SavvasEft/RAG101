import os

class DocumentCollector:
    def __init__(self, directory):
        self.directory = directory

    def collect(self):
        documents = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.txt'):  # Extend this for other file types
                full_path = os.path.join(self.directory, filename)
                documents.append((filename, full_path))
        return documents