import os
from dotenv import load_dotenv
import logging
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
embeddings = OpenAIEmbeddings()

class EmbeddingGeneration:
    def __init__(self, docpath):
        # Load the text file
        self.loader = TextLoader(file_path=docpath, encoding="utf-8")
        self.documents = self.loader.load()  # Returns a list of Document objects

    def embedding_gen(self):   
        # Extract raw text from Document objects
        text = "\n".join([doc.page_content for doc in self.documents])  # Convert to a single string
        
        # Use RecursiveCharacterTextSplitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=30,
            separators=["\n\n", "\n", " ", ""],
        )
        
        try:                
            split_documents = text_splitter.create_documents([text])  # Creates list of Document objects   
            # Generate embeddings and store in FAISS
            vectorstore = FAISS.from_documents(split_documents, embeddings)   
            print("Document embedded successfully!")
            # Save the vector store
            vectorstore.save_local("./embedding_doc/doc_faiss_index")
            print("Document embedding stored successfully!")
        except Exception as e:
            logging.error(f"Embedding and store error: {e}")  # Corrected error logging


class EmbeddingRetrieval:
    def __init__(self, embeddingpath):
        self.vectorstore = FAISS.load_local(
            embeddingpath, embeddings, allow_dangerous_deserialization=True
        )

    def retrieve_context(self, query, k=2):
        """Retrieve relevant contexts based on similarity search."""
        results = self.vectorstore.similarity_search(query, k=k)  # Fetch top-k matches
        return "\n".join([doc.page_content for doc in results]) if results else "No relevant context found."



