# Chatbot-with-PDF-DOCX-and-Image-Support

This project is a chatbot application that can process PDF, DOCX, and image files, allowing users to query text extracted from these files. It leverages Google's Gemini API to respond to user queries. The application is built using Streamlit and is designed to be user-friendly, providing an interactive chat interface.

## Features

- **Document Support**: Supports PDF, DOCX, and image files (JPG, PNG).
- **Summarization**: Summarizes the entire document or sections of it.
- **Multiple File Upload**: Supports uploading multiple files at once.
- **Gemini Integration**: Uses Google Gemini models for natural language queries.
- **File Export**: Users can download chat history as `.txt` or `.pdf`.
- **OCR (Optical Character Recognition)**: Extracts text from images using Tesseract OCR.

## Requirements

- Python 3.x
- Streamlit
- Gemini API key (free tier available at https://aistudio.google.com/apikey)
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

### 4. Get a Gemini API key
Create a free key at https://aistudio.google.com/apikey.

### 5. Set your key
Never put the key in the script. Use either:

- an environment variable: `export GEMINI_API_KEY=your_key`
- Streamlit secrets: copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add your key (the file is git-ignored)

The model defaults to `gemini-2.5-flash`; override it with `GEMINI_MODEL`.

### 6. Start the Streamlit App
Once you have completed the setup, run the following command to start the Streamlit app:

streamlit run pdf_chatbot_advanced.py






## Deploy on Streamlit Community Cloud
1. Push this repo to GitHub, then go to https://share.streamlit.io and choose **Create app**.
2. Select this repo, branch `main`, and main file `pdf_chatbot_advanced.py`.
3. Under **Advanced settings > Secrets**, paste `GEMINI_API_KEY = "your_key"`.
4. Deploy. `packages.txt` installs Tesseract so image OCR works.
