from splitter import split_document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FastEmbedEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = FastEmbedEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

def build_vector_store(file_path):
    chunks = split_document(file_path)

    vector_store = FAISS.from_documents(
        chunks,embedding_model)

    return vector_store
