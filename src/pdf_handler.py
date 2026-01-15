from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_document(pdf_path):
    """
    1. Loads a PDF.
    2. Splits it into chunks for the AI.
    Returns: A list of text chunks.
    """
    print(f"📄 Loading {pdf_path}...")
    
    # 1. Load the PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    
    # 2. Split the text
    # We cut text into 1000-character chunks with 200 chars overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks = text_splitter.split_documents(docs)
    
    print(f"✅ Success! Split document into {len(chunks)} chunks.")
    return chunks