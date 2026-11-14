import streamlit as st
import os
from fpdf import FPDF
from PyPDF2 import PdfReader
from PIL import Image
import docx
from google import genai
import json
import textwrap

# Gemini configuration: the key comes from Streamlit secrets or the GEMINI_API_KEY environment variable.
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MAX_DOC_CHARS = 60000  # keep the prompt within the model's context window


def get_client():
    try:
        key = st.secrets.get("GEMINI_API_KEY")
    except Exception:  # no secrets file present
        key = None
    key = key or os.getenv("GEMINI_API_KEY")
    if not key:
        st.error("Missing GEMINI_API_KEY. Add it to Streamlit secrets or your environment.")
        st.stop()
    return genai.Client(api_key=key)


# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Helper function to process and extract text from PDF, DOCX, or image
def process_file(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    extracted_text = ""

    if file_extension == "pdf":
        # Extract text from PDF
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            extracted_text += page.extract_text()
    elif file_extension in ["jpg", "jpeg", "png"]:
        # Extract text from Image using OCR
        image = Image.open(uploaded_file)
        extracted_text = image_to_text(image)
    elif file_extension == "docx":
        # Extract text from DOCX
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            extracted_text += para.text + "\n"
    else:
        extracted_text = uploaded_file.getvalue().decode("utf-8")
    
    return extracted_text

def image_to_text(image):
    import pytesseract
    return pytesseract.image_to_string(image)

# Function to query Gemini API for chatbot response
def query_gemini(question, document_text=""):
    prompt = "Answer using the provided document when one is given; say so if the answer is not in it.\n\n"
    if document_text:
        prompt += "Document:\n" + document_text[:MAX_DOC_CHARS] + "\n\n"
    prompt += "Question: " + question
    response = get_client().models.generate_content(model=MODEL, contents=prompt)
    return (response.text or "").strip()

# Display chat messages with styling
def display_chat(messages):
    for message in messages:
        if message['role'] == 'user':
            st.markdown(f"<div style='background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>User: {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #F1F0F0; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>Bot: {message['content']}</div>", unsafe_allow_html=True)

# Clear chat history
def clear_chat():
    st.session_state.messages = []

# Summarize the document using Gemini
def summarize_document(text):
    response = get_client().models.generate_content(
        model=MODEL, contents="Summarize the following document:\n" + text[:MAX_DOC_CHARS]
    )
    return (response.text or "").strip()

# Save chat history to PDF
def save_chat_history_to_pdf(messages):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for message in messages:
        pdf.multi_cell(0, 10, f"{message['role'].capitalize()}: {message['content']}")
    
    pdf_output = "chat_history.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Save chat history to text file
def save_chat_history_to_txt(messages):
    chat_history = "\n".join([f"{message['role'].capitalize()}: {message['content']}" for message in messages])
    
    txt_output = "chat_history.txt"
    with open(txt_output, 'w') as f:
        f.write(chat_history)
    
    return txt_output

# Main function to run the app
def main():
    st.title("Chatbot with PDF, DOCX, and Image Support")

    # Sidebar for file upload and chat history options
    st.sidebar.title("Options")
    uploaded_files = st.sidebar.file_uploader("Upload Files (PDF, DOCX, Image)", accept_multiple_files=True)
    
    if uploaded_files:
        all_text = ""
        for uploaded_file in uploaded_files:
            file_text = process_file(uploaded_file)
            all_text += file_text + "\n"
        st.session_state.text = all_text

        st.sidebar.markdown("### File Details")
        st.sidebar.markdown(f"**Uploaded Files**: {', '.join([file.name for file in uploaded_files])}")
        st.sidebar.markdown(f"**Text Length**: {len(all_text)} characters")
    
    # Chat area with input and messages
    user_input = st.text_input("Ask a question about the document:")
    if user_input:
        st.session_state.messages.append({'role': 'user', 'content': user_input})
        
        # Get response from Gemini
        response = query_gemini(user_input, st.session_state.get('text', ''))
        st.session_state.messages.append({'role': 'bot', 'content': response})
        
    # Display chat history
    display_chat(st.session_state.messages)
    
    # Summarize button
    if st.button("Summarize the Document"):
        if 'text' in st.session_state:
            summary = summarize_document(st.session_state.text)
            st.session_state.messages.append({'role': 'bot', 'content': f"Summary: {summary}"})
            display_chat(st.session_state.messages)

    # Clear chat history
    if st.sidebar.button("Clear Chat History"):
        clear_chat()
        st.rerun()

    # Download options
    if st.sidebar.button("Download Chat History as Text"):
        txt_file = save_chat_history_to_txt(st.session_state.messages)
        st.sidebar.download_button("Download Text File", txt_file, file_name="chat_history.txt")

    if st.sidebar.button("Download Chat History as PDF"):
        pdf_file = save_chat_history_to_pdf(st.session_state.messages)
        st.sidebar.download_button("Download PDF File", pdf_file, file_name="chat_history.pdf")

if __name__ == "__main__":
    main()
