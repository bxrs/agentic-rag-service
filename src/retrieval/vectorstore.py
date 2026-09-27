from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_vectorstore_retriever(data_dir: str = "data/raw"):
    # Load all .txt and .md files in the data/raw folder
    loader = DirectoryLoader(data_dir, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    # Split into manageable chunks (e.g., 500 characters with 50 overlap)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    
    # ... vector database indexing follows