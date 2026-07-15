import os
import shutil
import logging

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

from embeddings_file import build_vector_store
from prompt_model import chain

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {".pdf", ".txt", ".csv", ".docx"}

retrievers = {}

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")

async def upload_document(thread_id: str = Form(...),file: UploadFile = File(...)):

    extension = os.path.splitext(file.filename)[1].lower()
    
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail = f"Unsupported file type: {extension}")
    
    file_path = os.path.join(UPLOAD_DIR,f"{thread_id}_{file.filename}")

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    file.file.close()
    
    try:
        vector_store = build_vector_store(file_path)
        
        retrievers[thread_id] = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k":4,"fetch_k":16,"lambda_mult":0.5}
        )
        
    except Exception:
        logger.exception("Failed to process uploaded document.")
        raise HTTPException(status_code=500,detail = "Failed to process the document.")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
            
    return {"message": "Document Uploaded Successfully"}


@app.post("/ask")

async def ask_question(question: str = Form(...), thread_id: str = Form(...)):

    retriever = retrievers.get(thread_id)

    if retriever is None:
        raise HTTPException(status_code=400,detail="Please upload a document first.")

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    answer = chain.invoke({"context":context, "question":question
    })

    return {"answer":answer, "chunks":[doc.page_content for doc in docs]}