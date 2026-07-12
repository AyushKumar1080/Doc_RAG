import os
import shutil

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from embeddings_file import build_vector_store
from prompt_model import chain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_store = None


@app.post("/upload")

async def upload_document(file: UploadFile = File(...)):

    global vector_store

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as f:

        shutil.copyfileobj(file.file, f)

    vector_store = build_vector_store(file_path)

    return {
        "message": "Document Uploaded Successfully"
    }


@app.post("/ask")

async def ask_question(question: str = Form(...)):

    global vector_store

    if vector_store is None:

        return {
            "answer":"Please upload a document first."
        }

    retriever = vector_store.as_retriever(

        search_type="mmr",

        search_kwargs={

            "k":4,
            "fetch_k":16,
            "lambda_mult":0.5

        }

    )

    docs = retriever.invoke(question)

    context = "\n\n".join(

        doc.page_content

        for doc in docs

    )

    answer = chain.invoke({

        "context":context,

        "question":question

    })

    return {

        "answer":answer,

        "chunks":[

            doc.page_content

            for doc in docs

        ]

    }