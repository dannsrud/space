from fastapi import APIRouter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_chroma import Chroma

from models.models import llm
# import chromadb
# from configs.chroma_config import chroma_configs
from models.models import embeddings
from prompts.prompts import rag_prompt
# from schemas.qa_schemas import QueryModel
from configs.config import chroma_client


router = APIRouter(prefix="/qa")

# chroma_client = chromadb.HttpClient(  # 이렇게 중복되서 사용하는건 db.py 같이 따로 만들어 두는 걸 추천한다.
#     host = chroma_configs['host'],
#     port = chroma_configs['port']
# )
# async def query(querymodel:QueryModel) # 이렇게 할때는 post로 날려야한다. 토큰값도 보내야해 강사님은 보통 포스트로 보낸다.

@router.get('/query', status_code=200)
async def query(collection_name : str, query: str): # get일 경우 이렇게 동작시키는게 맞다. # get URL 에 넣어서 보냄 / post body에 넣어서 보냄.
    chromaDB = Chroma(
        embedding_function = embeddings,
        collection_name = collection_name,
        client = chroma_client

    )
    # chroma -> 
    retriever = chromaDB.as_retriever(
        search_type = "similarity_score_threshold",
        search_kwargs = {"k": 5, "score_threshold": 0.6}
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    llm_chain = {"question": RunnablePassthrough(),
                 "context": RunnablePassthrough() | retriever | format_docs
                } | rag_prompt | llm | StrOutputParser()
    res = llm_chain.invoke(query)
    return {"response":res}