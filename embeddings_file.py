from splitter import split_document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

def build_vector_store(file_path):
    chunks = split_document(file_path)

    vector_store = FAISS.from_documents(
        chunks,embedding_model)

    return vector_store
