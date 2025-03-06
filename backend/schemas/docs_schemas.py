from pydantic import BaseModel
class InsertModel(BaseModel):
    collection_name : str
    pdf_path: str