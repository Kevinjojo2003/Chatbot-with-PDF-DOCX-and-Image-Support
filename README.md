# Chatbot-with-PDF-DOCX-and-Image-Support

This project is a chatbot application that can process PDF, DOCX, and image files, allowing users to query text extracted from these files. It leverages OpenAI's GPT API to respond to user queries. The application is built using Streamlit and is designed to be user-friendly, providing an interactive chat interface.

For Preview : "https://chatbot-with-pdf-docx-and-image-support-nz3f4iorwuqujz2v6sncxm.streamlit.app/"
## Features

- **Document Support**: Supports PDF, DOCX, and image files (JPG, PNG).
- **Summarization**: Summarizes the entire document or sections of it.
- **Multiple File Upload**: Supports uploading multiple files at once.
- **OpenAI Integration**: Uses GPT-based models for natural language queries.
- **File Export**: Users can download chat history as `.txt` or `.pdf`.
- **OCR (Optical Character Recognition)**: Extracts text from images using Tesseract OCR.

## Requirements

- Python 3.x
- Streamlit
- OpenAI API key
- Tesseract OCR (for image text extraction)
- Required Python libraries

## Setup

Follow these steps to set up and run the chatbot:

### 1. Clone the Repository

First, clone the repository to your local machine:

### 2. Install Python Dependencies
Install the required Python libraries by running the following command:

pip install -r requirements.txt

### 3. Install Tesseract OCR
Tesseract OCR is needed for image-to-text conversion. You can install it based on your operating system:

For Windows:
Follow the installation instructions  https://github.com/tesseract-ocr/tesseract .

Once installed, make sure Tesseract is added to your system's PATH.

### 4. Obtain OpenAI API Key
You will need an OpenAI API key to interact with the GPT model. Here's how to obtain one:

Go to the OpenAI API website.
Sign up or log in.
After logging in, navigate to the API section and generate a new API key.
Copy the API key.

### 5. Set Your OpenAI API Key
Method 1: Set the API Key in the Script
You can manually set the OpenAI API key in the pdf_chatbot_advanced.py script. Open the script and look for the following line:

### 6. Start the Streamlit App
Once you have completed the setup, run the following command to start the Streamlit app:

streamlit run pdf_chatbot_advanced.py




