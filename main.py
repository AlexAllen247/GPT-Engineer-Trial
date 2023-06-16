import streamlit as st
from pdf_document import PDFDocument
from chatbot import Chatbot

class StreamlitApp:
    def __init__(self, pdf_path: str, chatbot: Chatbot):
        self.pdf_doc = PDFDocument(pdf_path)
        self.chatbot = chatbot

    def run(self):
        st.title("PDF Chatbot")
        st.sidebar.title("PDF Document")
        st.sidebar.text_input("Enter PDF path:", value=self.pdf_doc.path, key="pdf_path")
        self.pdf_doc.load()
        st.sidebar.text_area("PDF Text", value=self.pdf_doc.text, height=600)
        st.sidebar.title("Chatbot")
        user_input = st.text_input("You:", key="user_input")
        if user_input:
            response = self.chatbot.generate_response(user_input, self.pdf_doc.embeddings)
            st.text_area("Chatbot:", value=response, height=200)

if __name__ == "__main__":
    chatbot = Chatbot()
    app = StreamlitApp("example.pdf", chatbot)
    app.run()