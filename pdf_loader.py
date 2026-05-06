# pdf_loader.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# PDF padhne ka function
def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    print(f"Pages loaded: {len(pages)}")
    return pages

# PDF ko chunks mein todna
def split_pdf(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,   # ek chunk = 500 characters
        chunk_overlap=50  # chunks ke beech thoda overlap
    )
    chunks = splitter.split_documents(pages)
    print(f"Chunks banaye: {len(chunks)}")
    return chunks

# Chunks ko FAISS database mein store karna
def create_vectorstore(chunks):

    # Ollama embeddings use karenge
    # Embeddings = text ko numbers mein badlna
    # Taaki AI compare kar sake
    embeddings = OllamaEmbeddings(
        model="llama3"  # same model jo tune download kiya
    )

    # FAISS database banao in chunks se
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Database disk pe save karo
    vectorstore.save_local("faiss_index")

    print("Vector database ready!")
    return vectorstore