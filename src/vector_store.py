from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_vectorstore(chunks):
    """
    Stores data in ChromaDB using a LOCAL Embedding Model.
    Benefit: No API Key required, No Rate Limits, 100% Free.
    """
    print("🧠 Initializing Local Embedding Model (HuggingFace)...")
    
    # 1. Initialize the Local Model
    # "all-MiniLM-L6-v2" is a famous, fast, and light model for laptops
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Setup the DB location
    persist_directory = "./chroma_db"
    
    print("💾 Saving to ChromaDB (This runs on your PC, might take a moment)...")
    
    # 3. Create/Update the Vector Store
    # Since it's local, we don't need batching or sleep timers! 🚀
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print("✅ Knowledge Base Build Complete!")
    return vectorstore