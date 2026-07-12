from langchain_community.document_loaders import (
    PyPDFLoader,TextLoader,CSVLoader,Docx2txtLoader
)
from pathlib import Path

def load_document(file_path):
    extension = Path(file_path).suffix.lower()
    
    if extension == '.pdf':
        loader = PyPDFLoader(file_path)
    elif extension == '.csv':
        loader = CSVLoader(file_path)
    elif extension == '.txt':
        loader = TextLoader(file_path)
    elif extension == '.docx':
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"This file type not supported by application: {extension}")
    
    return loader.load()
