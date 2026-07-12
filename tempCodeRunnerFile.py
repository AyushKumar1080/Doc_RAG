from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, reply:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}                               
""")

llm = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()
chain = prompt | llm | parser
