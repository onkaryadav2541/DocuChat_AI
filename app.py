import streamlit as st
import os
from src.pdf_handler import process_document

st.set_page_config(page_title="DocuChat AI", page_icon="📄")

st.title("📄 DocuChat AI")
st.caption("Private RAG System | Built by Onkar Yadav")

uploaded_file = st.file_uploader("Upload a PDF Document", type="pdf")

if uploaded_file:
    # Save file temporarily so PyPDF can read it
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Processing document..."):
        chunks = process_document("temp.pdf")
        
    st.success(f"✅ Document Processed! Split into {len(chunks)} chunks.")
    
    # Show the first chunk to prove it works
    st.info("👇 AI 'Vision' (What the system reads):")
    st.code(chunks[0].page_content)
    
    # Cleanup
    os.remove("temp.pdf")