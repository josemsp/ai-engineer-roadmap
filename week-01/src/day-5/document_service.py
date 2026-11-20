from document import Document

class DocumentService:
    def __init__(self):
        self.documents: dict[int, Document] = {}
    
    def create_document(
        self,
        document_id: int,
        name: str,
        category: str,
        content: str        
    ) -> Document:
        if document_id in self.documents:
            raise ValueError("Document already exists")
        
        document = Document(
            id=document_id,
            name=name,
            category=category,
            content=content
        )
        
        self.documents[document_id] = document
        
        return document
    
    def get_document(
        self, 
        document_id:int
    ) -> Document | None:
        return self.documents.get(document_id)
    
    def get_all_documents(self) -> list[Document]:
        return list(self.documents.values())
    
    def process_document(self, document_id:int) -> bool:
        document = self.get_document(document_id)
        
        if document is None:
            return False
        
        document.add_chunk(document.content)
        document.mark_as_processed()
        
        return True

        
        
        
