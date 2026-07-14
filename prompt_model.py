from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Use ONLY the information provided in the context to answer the user's question.

If the answer cannot be found in the context, respond exactly with:
"I couldn't find that information in the uploaded documents."

Do not make up information.
Do not use outside knowledge.

Context:
{context}

Question:
{question}
""")

llm = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()
chain = prompt | llm | parser
