from splitter import split_document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FastEmbedEmbeddings

embedding_model = FastEmbedEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

def build_vector_store(file_path: str)->FAISS:
    """
    Load a document, split it into chunks and create a FAISS vector store.
    """
    chunks = split_document(file_path)

    return FAISS.from_documents(
        documents=chunks,embedding=embedding_model)

