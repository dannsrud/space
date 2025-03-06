from fastapi import APIRouter
from langchain_chroma import Chroma

# import chromadb
# from configs.chroma_config import chroma_configs
from models.models import embeddings
from schemas.docs_schemas import InsertModel
from typing import Union
from langchain_community.document_loaders import PyMuPDFLoader
from glob import glob
import os
from configs.config import chroma_client


router = APIRouter(prefix = "/docs")
# chroma_client = chromadb.HttpClient(
#     host = chroma_configs['host'],
#     port = chroma_configs['port']
# )

@router.post("/insert", status_code=200)
async def insert(insert_model:InsertModel):
    pdf_path = insert_model.pdf_path
    collection_name = insert_model.collection_name

    print("pdf_path", pdf_path)
    print("collection_name", collection_name)

    chromaDB = Chroma(
        embedding_function = embeddings,
        collection_name = collection_name,
        client = chroma_client

    )
    pdf_path_list = glob(os.path.join(pdf_path, "*.pdf"))
    print("pdf_file_list", pdf_path_list)
    pdf_data_list = []
    for pdf_path in pdf_path_list:
        loader = PyMuPDFLoader(pdf_path)
        pdf_data = loader.load()
        pdf_data_list.extend(pdf_data)

    chromaDB.add_documents(pdf_data_list)

    return {"response":"OK"}

# 웹페이지에서 긁어오는 방식이 아닌 한 폴더 안에있는 전체 PDF파일을 모두 불러오는 방식임.