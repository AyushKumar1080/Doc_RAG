import tempfile

import streamlit as st

from embeddings_file import build_vector_store
from prompt_model import chain

st.title("Hybrid RAG")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf","txt","csv","docx"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="."+uploaded_file.name.split(".")[-1]
    ) as tmp:

        tmp.write(uploaded_file.read())

        file_path = tmp.name

    vector_store = build_vector_store(file_path)

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":4,
            "fetch_k":16,
            "lambda_mult":0.5
        }
    )

    query = st.text_input("Ask a question")

    if st.button("Submit"):

        docs = retriever.invoke(query)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        answer = chain.invoke({
            "context": context,
            "question": query
        })

        st.subheader("Answer")

        st.write(answer)

        with st.expander("Retrieved Chunks"):

            for doc in docs:
                st.write(doc.page_content)
                st.divider()