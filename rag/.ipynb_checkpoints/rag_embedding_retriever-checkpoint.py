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


import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config')  # Assuming the file is named 'config'

# # Fetch the variables
EMBEDDING_PATH = config['DEFAULT']['EMBEDDING_PATH'].strip('"')


class EmbeddingRetrieval:
    def __init__(self, embeddingpath):
        self.vectorstore = FAISS.load_local(
            embeddingpath, embeddings, allow_dangerous_deserialization=True
        )

    def retrieve_context(self, query, k=2):
        """Retrieve and print relevant contexts based on similarity search."""
        results = self.vectorstore.similarity_search(query, k=k)  # Fetch top-k matches
        context = "\n".join([doc.page_content for doc in results]) if results else "No relevant context found."
        # print("\n=== Retrieved Context ===\n", context)  # Print the relevant context
        return context

# Initialize retriever
retriever_instance = EmbeddingRetrieval(EMBEDDING_PATH)

# Example usage
query = "what is a malware?"
print("Context: ", retriever_instance.retrieve_context(query))