import chromadb
# from configs.chroma_config import chroma_configs
import os

CHROMA_HOST = os.getenv("CHROMA_HOST")
CHROMA_PORT = os.getenv("CHROMA_PORT")

chroma_client = chromadb.HttpClient(  # 이렇게 중복되서 사용하는건 db.py 같이 따로 만들어 두는 걸 추천한다.
    host = CHROMA_HOST,
    port = CHROMA_PORT
)
