# Hybrid RAG using LangChain + FAISS + Hugging Face

## Overview

This project implements a **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** pipeline using **LangChain**, **FAISS**, and **Hugging Face Embeddings**. It enables users to query one or more documents and receive context-aware answers from a Large Language Model (LLM).

The pipeline combines document loading, text chunking, embedding generation, vector search, and LLM-based response generation.

---

## Features

* Load multiple document formats

  * PDF
  * TXT
  * DOCX
* Automatic text chunking
* Hugging Face embedding generation
* FAISS vector database
* Semantic similarity search
* Context-aware answer generation
* Easy to extend with additional document loaders

---

## Tech Stack

* Python 3.10+
* LangChain
* Hugging Face Transformers
* BAAI/bge-base-en-v1.5 Embeddings
* FAISS
* PyTorch

---

## Workflow

1. Load documents.
2. Split documents into chunks.
3. Generate embeddings.
4. Store embeddings in FAISS.
5. Retrieve the most relevant chunks.
6. Pass retrieved context to the LLM.
7. Generate the final answer.

---

## Supported File Types

File types: (.csv), (.txt), (.pdf), (.docx)

---

## Example

User Question:

```
What is Retrieval-Augmented Generation?
```

Pipeline:

```
Question
      │
      ▼
Vector Search
      │
      ▼
Relevant Chunks
      │
      ▼
LLM
      │
      ▼
Final Answer
```

---

## Future Improvements

* Hybrid search (Dense + BM25)
* Cross-encoder reranking
* Persistent vector database (Chroma, Milvus, Pinecone)
* Streamlit or Gradio interface
* Conversation memory
* Multi-document querying
* Source citations
* Metadata filtering


---

## Acknowledgements

* LangChain
* Hugging Face
* FAISS
* BAAI
* PyTorch
