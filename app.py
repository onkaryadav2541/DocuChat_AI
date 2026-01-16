import streamlit as st
import os
import shutil
from src.pdf_handler import process_document
from src.vector_store import get_vectorstore
import src.config # Imports env variables

st.set_page_config(page_title="DocuChat AI", page_icon="🤖")

st.title("🤖 DocuChat AI")
st.caption("Enterprise RAG System | Build Your Corporate Knowledge Base")

# --- SIDEBAR: The Input Zone ---
with st.sidebar:
    st.header("📂 Knowledge Base")
    st.write("Upload company documents here to train the AI.")
    
    # 1. Allow Multiple Files
    uploaded_files = st.file_uploader(
        "Upload PDFs", 
        type="pdf", 
        accept_multiple_files=True
    )
    
    process_btn = st.button("Build Brain 🧠")

# --- MAIN LOGIC ---
if process_btn and uploaded_files:
    st.info("🚀 Starting Ingestion Pipeline...")
    
    all_chunks = []
    
    # Create a temp folder for processing
    if not os.path.exists("temp_docs"):
        os.makedirs("temp_docs")
        
    progress_bar = st.progress(0)
    
    # Loop through every file uploaded
    for i, file in enumerate(uploaded_files):
        # Update progress bar
        progress = (i + 1) / len(uploaded_files)
        progress_bar.progress(progress)
        
        # Save bytes to a real file path
        temp_path = os.path.join("temp_docs", file.name)
        with open(temp_path, "wb") as f:
            f.write(file.getbuffer())
            
        # Process ONLY this file
        chunks = process_document(temp_path)
        all_chunks.extend(chunks) # Add to the big pile
        
    st.write(f"✅ Processed {len(uploaded_files)} files.")
    st.write(f"🔢 Total Chunks Generated: {len(all_chunks)}")
    
    # BUILD THE BRAIN
    with st.spinner("🧠 Embedding data into Vector Store..."):
        get_vectorstore(all_chunks)
        
    st.success("🎉 Brain Built! The AI now knows this data.")
    
    # Cleanup: Remove temp files
    shutil.rmtree("temp_docs")

else:
    st.info("👈 Upload documents in the sidebar to start.")