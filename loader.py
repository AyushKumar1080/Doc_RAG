from langchain_community.document_loaders import (
    PyPDFLoader,TextLoader,CSVLoader,Docx2txtLoader
)
from pathlib import Path

def load_document(file_path: str):
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    extension = file_path.suffix.lower()
    
    if extension == '.pdf':
        loader = PyPDFLoader(str(file_path))
    elif extension == '.csv':
        loader = CSVLoader(str(file_path))
    elif extension == '.txt':
        loader = TextLoader(str(file_path))
    elif extension == '.docx':
        loader = Docx2txtLoader(str(file_path))
    else:
        raise ValueError(f"This file type not supported by application: {extension}")
    
    return loader.load()
