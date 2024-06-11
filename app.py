from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter

def main():
    load_dotenv()
    #print(os.getenv("OPENAI_API_KEY"))
    print("Heloo AI Custom RAG pretrained PDF Cahat bot!!@@@@@")
    st.set_page_config(page_title = "Ask your PDF")
    st.header("Ask your PDF 💬")
    
    #uploading file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    #extract the text from pdf                       
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text =""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # split in to chunks with Langgchain
        text_splitter = CharacterTextSplitter(
         separator = "\n",
         chunk_size = 200,
         chunk_overlap = 20,
         length_function = len
         )
        chunks = text_splitter.split_text(text)

        st.write(chunks)
    
if __name__ =='__main__':
    main()