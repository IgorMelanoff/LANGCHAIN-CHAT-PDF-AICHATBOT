from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv()
    print("///// API key: ///////////////////////")
    print(os.getenv("OPENAI_API_KEY"))
    print("//////////////////////////////////////")
    st.set_page_config(page_title = "Ask your PDF")
    st.header("Ask your PDF 💬")
    
    #uploading file
    print("///// Uploading file ///////////////////////")
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    #extract the text from pdf
    print("///// Extracting the text from PDF ///////////////////////")                       
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text =""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # split in to chunks with Langchain
        print("///// Splitting in to chunks with Langchain ///////////////////////")  
        text_splitter = CharacterTextSplitter(
         separator = "\n",
         chunk_size = 1000,
         chunk_overlap = 200,
         length_function = len
         )
        chunks = text_splitter.split_text(text)
        #st.write(chunks)

        #create embeddings
        print("///// Creating Embeddings ///////////////////////")
        embeddings = OpenAIEmbeddings()
        #similarity search - fasebook libraies and finishing the Knowlege Base
        print("///// Using Langchain fasebook FAISS Vector libraies create the Knowlege Base ///////////////////////")
        knowlege_base = FAISS.from_texts(chunks, embeddings)
        #st.write(knowlege_base)
        
        #user interact UI - show user input - catching question
        print("///// Cathing Question for User  ///////////////////////")
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            print("//////////Similarity semantic search////////////////////////////////")
            docs = knowlege_base.similarity_search(user_question)
            st.write(docs)
            print("//////////use Langchain as the wrapper for LLM(GPT) for answer user questions ////////////////////////////////")
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents = docs, question=user_question)
                print("//////////OpenAPI Usage 💰🤑💵/////////")
                print(cb)
            st.write(response)



    
if __name__ =='__main__':
    main()