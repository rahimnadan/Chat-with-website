import os
import streamlit as st
from langchain.chains import RetrievalQA
from bs4 import BeautifulSoup
from langchain.prompts.chat import (ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
import requests

# Define the system template for answering questions
system_template = """Use the following pieces of context to answer the user's question. 
     If you don't know the answer, just say that you don't know, don't try to make up an answer."""


messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]


prompt = ChatPromptTemplate.from_messages(messages)

def main():
    st.set_page_config(page_title="Chat With Website", layout="wide")

    
    st.title('🦜🔗 Chat With Website')
    st.markdown("""
    This chatbot extracts text from a specified website in real time and answers questions about the content provided.
    You can ask questions related to the website content and get accurate responses based on the extracted data.\n
    For example, you might ask questions like ***"What is the main topic of this page?"*** or,\n
    ***"Can you summarize the key points?"***.\n
    You Can Contact me [on LinkedIn](https://www.linkedin.com/in/abdur-rahim-718ba4227).
    If You need my services, Here is [My Upwork](https://www.upwork.com/freelancers/~01b89f620c7324a467)
    """)
    st.sidebar.title('🔗Input your website URL')
    st.sidebar.write('***Ask questions below, and receive answers directly from the website.***')

    
    url = st.sidebar.text_input("Insert the website URL")

    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    
    user_question = st.chat_input("Ask a question (query/prompt)")

    if user_question and url:
        os.environ['GOOGLE_API_KEY'] = "AIzaSyA0S7F21ExbBnR06YXkEi7aj94nWP5kJho"  
        
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        
        text = soup.get_text(separator='\n')
        
        
        text_splitter = CharacterTextSplitter(separator='\n', chunk_size=512, chunk_overlap=100)
        docs = text_splitter.split_text(text)

        
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        
        vectordb = FAISS.from_texts(texts=docs, embedding=embeddings)

        
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})

        
        llm = ChatGroq(model="llama3-70b-8192", groq_api_key="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")

        # Create a RetrievalQA instance from the model and retriever
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

        # Include chat history in the query
        full_query = {
            "query": user_question,
            "chat_history": st.session_state.chat_history
        }

        # Run the user's question through the RetrievalQA and get the response
        response = qa.invoke(full_query)
        
        # Update the chat history
        st.session_state.chat_history.append({"query": user_question, "response": response['result']})

        # Refresh the page to display the new chat message
        st.experimental_rerun()

    # Display the chat history in a structured manner
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history:
            user_col, bot_col = st.columns([1, 3])
            with user_col:
                st.markdown(f"😃 **You:**")
                st.markdown(f"<div style='background-color: #FFC0CB; padding: 10px; border-radius: 10px;'>{entry['query']}</div>", unsafe_allow_html=True)
            with bot_col:
                st.markdown(f"🤖 **Bot:**")
                st.markdown(f"<div style='background-color: #FFD700; padding: 10px; border-radius: 10px;'>{entry['response']}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
