# 📚 Hybrid RAG: AI-Powered Document Question Answering

An end-to-end **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** application that enables users to upload documents and ask natural language questions. The system retrieves the most relevant document chunks using **FAISS vector search** and generates context-aware answers using a **Large Language Model (LLM)**.

The application is built with **FastAPI** for the backend and **Streamlit** for the frontend, supporting multiple document formats and thread-based user sessions.

---

## 🚀 Features

- 📄 Upload multiple document formats
  - PDF
  - TXT
  - CSV
  - DOCX
- ✂️ Automatic document chunking
- 🔎 Semantic document retrieval using FAISS
- 🤖 AI-powered question answering using Groq LLM
- 🧠 FastEmbed embeddings (BAAI/bge-small-en-v1.5)
- 🔄 Maximum Marginal Relevance (MMR) retrieval
- 💬 Thread-based user sessions for isolated conversations
- 🌐 FastAPI REST API
- 🎨 Interactive Streamlit interface
- 📦 Modular project architecture
- 🔒 Environment variable support using `.env`

---

## 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Upload Document (Streamlit)
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
          Document Loader
                  │
                  ▼
         Recursive Splitter
                  │
                  ▼
       FastEmbed Embeddings
                  │
                  ▼
         FAISS Vector Store
                  │
                  ▼
       MMR Semantic Retrieval
                  │
                  ▼
              Groq LLM
                  │
                  ▼
          Context-Aware Answer
```

---

## ⚙️ Technologies Used

- Python 3.10+
- LangChain
- FastAPI
- Streamlit
- FAISS
- FastEmbed
- Groq API
- Hugging Face Embeddings
- Pydantic
- python-dotenv

---

## 🔄 Workflow

### Step 1 – Upload Document

The user uploads one of the supported document types.

### Step 2 – Document Processing

- Load document
- Split into overlapping chunks
- Generate vector embeddings

### Step 3 – Vector Storage

Chunks are stored inside a FAISS vector database.

### Step 4 – Retrieval

Maximum Marginal Relevance (MMR) retrieves the most relevant chunks.

### Step 5 – Answer Generation

Retrieved context is passed to the LLM, which generates an accurate answer using only the provided context.

---

## 📁 Supported File Types

- PDF (.pdf)
- Text (.txt)
- CSV (.csv)
- Microsoft Word (.docx)

---

## 📸 Example

### User Question

```
What is Retrieval-Augmented Generation?
```

### Processing Pipeline

```
Question
     │
     ▼
Semantic Retrieval
     │
     ▼
Relevant Chunks
     │
     ▼
Groq LLM
     │
     ▼
Generated Answer
```

---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/AyushKumar1080/Doc_RAG.git

cd Doc_RAG
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Backend

```bash
uvicorn backend:app --reload
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend.py
```

---

## 💡 Future Improvements

- LangGraph-based conversational RAG
- Persistent conversation memory
- Hybrid Search (Dense + BM25)
- Cross-Encoder Re-ranking
- ChromaDB / Pinecone integration
- Source citations with page numbers
- Streaming LLM responses
- Chat history sidebar
- Multi-document knowledge base
- Authentication and user management
- Docker support
- Cloud deployment with CI/CD

---

## 📌 Acknowledgements

- LangChain
- FastAPI
- Streamlit
- Groq
- FAISS
- Hugging Face
- FastEmbed
- BAAI

---

## 👨‍💻 Author

**Ayush Kumar**

B.Tech – Computer Science & Engineering  
National Institute of Technology Durgapur

GitHub: https://github.com/AyushKumar1080

