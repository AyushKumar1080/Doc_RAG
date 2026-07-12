from langchain_huggingface import HuggingFaceEmbeddings
from splitter import split_document
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

def build_vector_store(file_path):
    chunks = split_document(file_path)

    vector_store = FAISS.from_documents(
        chunks,embedding_model)

    return vector_store
