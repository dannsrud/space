from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# import tiktoken


# file load
file_name = []  # 5개의 file 모두 들어갈수있게 추가 세팅해야함.

dir_path = "../data/law_documents/"
file_path = "1_buildingAct.pdf"

full_path = dir_path + file_path

loader = PyMuPDFLoader(full_path)
pdf_data = loader.load()

# chunking
# def length_function(input_text):
#     tiktoken_text = tiktoken.tokenize(input_text)
#     return len(tiktoken_text)

chunk_size = 200 # 너무 잘게 조개면 가져와야하는 데이터가 너무 잘게 되어있어 지양하는게 좋다.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = chunk_size,
    chunk_overlap = int(chunk_size * 0.2),
    length_function = len
)

splitted_data = text_splitter.split_documents(pdf_data)

print(splitted_data[0])


# embeddings

