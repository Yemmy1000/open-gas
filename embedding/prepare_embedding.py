import os
import logging
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS



class EmbeddingGeneration:
    def __init__(self, folder_path, embeddings):
        self.folder_path = folder_path
        self.embeddings = embeddings
        self.documents = self.load_all_pdfs()

    def load_all_pdfs(self):
        documents = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if file.lower().endswith('.pdf'):
                    pdf_path = os.path.join(root, file)
                    try:
                        loader = PyPDFLoader(pdf_path)
                        docs = loader.load()
                        documents.extend(docs)
                    except Exception as e:
                        logging.error(f"Failed to load {pdf_path}: {e}")
        return documents

    def embedding_gen(self):
        if not self.documents:
            logging.error("No PDF documents found to embed.")
            return

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=30,
            separators=["\n\n", "\n", " ", ""],
        )

        try:
            split_documents = text_splitter.split_documents(self.documents)
            vectorstore = FAISS.from_documents(split_documents, self.embeddings)
            print("Documents embedded successfully!")
            vectorstore.save_local("../embedded_doc/doc_faiss_index")
            print("Document embeddings stored successfully!")
        except Exception as e:
            logging.error(f"Embedding and store error: {e}")


if __name__ == "__main__":
    from langchain_openai import OpenAIEmbeddings
    import configparser

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config file
    config.read('config')  # Assuming the file is named 'config'

    # # Fetch the variables
    DOCUMENT_PATH = config['DEFAULT']['DOCUMENT_PATH'].strip('"')

    # Initialize embeddings
    embeddings = OpenAIEmbeddings()

    # Specify the folder containing PDF files
    # folder_path = "../document/pdf_doc"
    folder_path = DOCUMENT_PATH

    # Create an instance of EmbeddingGeneration
    embedding_gen = EmbeddingGeneration(folder_path, embeddings)

    # Generate embeddings
    embedding_gen.embedding_gen()