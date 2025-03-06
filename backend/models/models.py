from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

# from configs.llm_api_configs import OPENAI_API_KEY
import os
from dotenv import load_dotenv

# os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
llm = ChatOpenAI(
        temperature = 0.1, # 창의성 (0.0 ~ 2.0)
        model_name = "gpt-4o-mini"
    )