from dataclasses import dataclass, field

@dataclass
class Document:
    id: int
    name: str
    category: str
    content: str
    chunks: list[str] = field(default_factory=list) # default new list in each instance
    processed: bool = False
    
    def mark_as_processed(self):
        self.processed = True
        
    def add_chunk(self, chunk:str):
        if not chunk.strip():
            raise ValueError("Chunk cannot be empty")
        
        self.chunks.append(chunk)

