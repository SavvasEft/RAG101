import os
from pymongo import MongoClient
from datetime import datetime

class DocumentMetadata:
    def __init__(self, filename, path, processed_date, chunk_count):
        self.filename = filename
        self.path = path
        self.processed_date = processed_date
        self.chunk_count = chunk_count

class DocumentManager:
    def __init__(self, db_name='rag_system', collection_name='documents'):
        from pymongo import MongoClient
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_document(self, filename, path, chunks):
        metadata = DocumentMetadata(
            filename=filename,
            path=path,
            processed_date=datetime.now(),
            chunk_count=len(chunks)
        )
        document = {
            "filename": metadata.filename,
            "path": metadata.path,
            "processed_date": metadata.processed_date,
            "chunk_count": metadata.chunk_count,
            "chunks": chunks
        }
        self.collection.insert_one(document)


    def document_exists(self, filename, path):
        return self.collection.find_one({"filename": filename, "path": path}) is not None

    def update_document(self, filename, path, chunks):
        metadata = DocumentMetadata(
            filename=filename,
            path=path,
            processed_date=datetime.now(),
            chunk_count=len(chunks)
        )
        document = {
            "filename": metadata.filename,
            "path": metadata.path,
            "processed_date": metadata.processed_date,
            "chunk_count": metadata.chunk_count,
            "chunks": chunks
        }
        self.collection.update_one(
            {"filename": filename, "path": path},
            {"$set": document},
            upsert=True
        )

    def get_all_documents(self):
        return list(self.collection.find())
    
    def get_document(self, filename, path):
        return self.collection.find_one({"filename": filename, "path": path})
    
    def reset_database(self):
        """
        Resets the database by dropping all collections.
        """
        for collection_name in self.db.list_collection_names():
            self.db.drop_collection(collection_name)
        print(f"All collections in the '{self.db.name}' database have been dropped.")

    def close(self):
        self.client.close()