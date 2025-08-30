import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def load_data(data_dir):
    """Load all PDFs from a directory."""
    loader = DirectoryLoader(
        data_dir,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    return loader.load()

def split_data(documents, chunk_size=500, chunk_overlap=20):
    """Split documents into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def load_embeddings(model="intfloat/multilingual-e5-base"):
    """Load embedding model (E5 by default)."""
    return HuggingFaceEmbeddings(model_name=model)

def build_index(embeddings, text_chunks, faiss_path="faiss_index"):
    """Build FAISS index from chunks and save locally."""
    print("✨ Creating new FAISS index...")
    docs = [Document(page_content=f"passage: {chunk.page_content}") for chunk in text_chunks]
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(faiss_path)
    print("💾 Saved FAISS index locally!")
    return vectorstore

def load_index(embeddings, faiss_path="faiss_index"):
    """Load an existing FAISS index."""
    if not os.path.exists(faiss_path):
        raise FileNotFoundError("❌ No FAISS index found. Please build it first.")
    print("🔄 Loading existing FAISS index...")
    return FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)


def load_llm(model_name="gpt-3.5-turbo-0125"):
    """Load OpenAI LLM."""
    return ChatOpenAI(
        model_name=model_name,
        temperature=0.3,
        max_tokens=200
    )

__all__ = ["load_data", "split_data", "load_embeddings", "build_index", "load_index", "load_llm"]
