from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_document

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

def split_document(file_path):
    documents = load_document(file_path)
    chunks = splitter.split_documents(documents)
    return chunks
