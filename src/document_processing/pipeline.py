class ProcessingPipeline:
    def __init__(self, loader, processor, chunker):
        self.loader = loader
        self.processor = processor
        self.chunker = chunker

    def process(self, document_path):
        content = self.loader.load(document_path)
        processed_text = self.processor.process(content)
        chunks = self.chunker.chunk(processed_text)
        return chunks