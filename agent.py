# agent.py

from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Database load karna
def load_vectorstore():

    # Same embeddings model use karo
    embeddings = OllamaEmbeddings(
        model="llama3"
    )

    # Disk se database load karo
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("Database loaded!")
    return vectorstore

# AI Agent banana
def create_agent(vectorstore):

    # Ollama ka llama3 model use karenge
    llm = ChatOllama(
        model="llama3",
        temperature=0  # 0 = zyada accurate answers
    )

    # RetrievalQA chain
    # Yeh chain PDF se relevant chunks dhundti hai
    # Phir llama3 se answer banati hai
    agent = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # top 3 chunks dhundo
        )
    )

    return agent

# Question poochna
def ask_question(agent, question):
    print(f"Sawal: {question}")
    answer = agent.invoke(question)
    print(f"Jawab: {answer['result']}")
    return answer['result']