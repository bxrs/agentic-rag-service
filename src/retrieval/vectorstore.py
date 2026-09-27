from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

PERSIST_DIR = "data/chroma_db"

def get_vectorstore_retriever(data_dir: str = "data/raw", force_rebuild: bool = False):
    """
    Builds (or loads a cached) Chroma vector store and returns a retriever.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # If we've already built the index and aren't forcing a rebuild, just load it
    if os.path.exists(PERSIST_DIR) and not force_rebuild:
        print("--- VECTORSTORE: LOADING EXISTING INDEX ---")
        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embeddings,
        )
        return vectorstore.as_retriever(search_kwargs={"k": 4})

    print("--- VECTORSTORE: BUILDING NEW INDEX ---")

    # Load all .txt files in the data/raw folder
    loader = DirectoryLoader(data_dir, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    if not docs:
        raise ValueError(
            f"No documents found in '{data_dir}'. Add some .txt files before building the index."
        )

    # Split into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # Embed + index
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )

    return vectorstore.as_retriever(search_kwargs={"k": 4})