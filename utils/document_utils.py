import tempfile
from datetime import datetime
from typing import List
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
import bs4

# Function to process PDFs
def process_pdf(file) -> List:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(file.getvalue())
            loader = PyPDFLoader(tmp_file.name)
            documents = loader.load()
            
            for doc in documents:
                doc.metadata.update({
                    "source_type": "pdf",
                    "file_name": file.name,
                    "timestamp": datetime.now().isoformat()
                })
            
            return documents
    except Exception as e:
        print(f"📄 PDF processing error: {str(e)}")
        return []

# Function to process web content
def process_web(url: str) -> List:
    try:
        loader = WebBaseLoader(
            web_paths=(url,),
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(
                    class_=("post-content", "post-title", "post-header", "content", "main")
                )
            )
        )
        documents = loader.load()
        return documents
    except Exception as e:
        print(f"🌐 Web processing error: {str(e)}")
        return []
