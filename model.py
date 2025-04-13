# Import necessary modules and classes
from langchain_community.vectorstores import Chroma
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 
from transformers import pipeline
import torch
from langchain.llms import HuggingFacePipeline
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Initialize a directory loader to load PDF documents from a directory
loader = DirectoryLoader("C:/Users/Hasan PC/OneDrive/Desktop/Final Year Project", glob="**/*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# Initialize a text splitter to split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)

# Split the loaded documents into chunks
texts = text_splitter.split_documents(documents)

# Creating a Vector DB using Chroma DB and SentenceTransformerEmbeddings
# Initialize SentenceTransformerEmbeddings with a pre-trained model
embeddings = SentenceTransformerEmbeddings(model_name="multi-qa-mpnet-base-dot-v1")

# Create a Chroma vector database from the text chunks
db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

# To save and load the saved vector db (if needed in the future)
# Persist the database to disk
# db.persist()
# db = Chroma(persist_directory="db", embedding_function=embeddings)

# Specify the checkpoint for the language model
checkpoint = "MBZUAI/LaMini-Flan-T5-783M"

# Initialize the tokenizer and base model for text generation
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint,
    device_map="auto",
    torch_dtype=torch.float32
)

# Initialize a local language model pipeline
local_llm = HuggingFacePipeline(pipeline=pipe)
# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=local_llm,
    chain_type='stuff',
    retriever=db.as_retriever(search_type="similarity", search_kwargs={"k": 2}),
    return_source_documents=True,
)


# Prompt the user for a query
input_query = str(input("Enter your query:"))

# Execute the query using the QA chain
llm_response = qa_chain({"query": input_query})

# Print the response
print(llm_response['result'])
