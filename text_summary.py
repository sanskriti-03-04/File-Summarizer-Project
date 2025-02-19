# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:44:54 2025

@author: sansk
"""
import streamlit as st
from transformers import pipeline
import fitz  # PyMuPDF for PDF extraction
import docx  # python-docx for DOCX extraction
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def extract_text_from_docx(docx_file):
    """Extract text from a DOCX file."""
    doc = docx.Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def summarize_text(text, max_length=150, min_length=50):
    """Generates a summary using an AI model."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
    return summary

def generate_pdf(summary):
    """Creates a PDF file with the summary text."""
    pdf_buffer = BytesIO()
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), summary, fontsize=12)
    doc.save(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

def main():
    st.set_page_config(page_title="Text Summarizer", layout="centered")
    st.title("📄 Text Summarizer")
    st.write("Upload a document (PDF/DOCX) or enter text to generate a summary.")
    
    # Sidebar controls
    st.sidebar.header("Summary Settings")
    max_length = st.sidebar.slider("Max Length", 50, 500, 150)
    min_length = st.sidebar.slider("Min Length", 20, 100, 50)
    
    # File uploader
    uploaded_file = st.file_uploader("Upload File (PDF/DOCX)", type=["pdf", "docx"])
    text = ""
    
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_extension == "docx":
            text = extract_text_from_docx(uploaded_file)
    
    # If no file is uploaded, allow manual text input
    text = text or st.text_area("Or Paste Your Text Here")
    
    if st.button("Summarize"):
        if text:
            summary = summarize_text(text, max_length, min_length)
            st.write("### ✨ Summary:")
            st.write(summary)
            
            # Option to download the summary as a text file
            st.download_button(label="Download Summary as TXT", data=summary, file_name="summary.txt", mime="text/plain")
            
            # Option to download the summary as a PDF
            pdf_buffer = generate_pdf(summary)
            st.download_button(label="Download Summary as PDF", data=pdf_buffer, file_name="summary.pdf", mime="application/pdf")
        else:
            st.error("Please enter text or upload a file.")

if __name__ == "__main__":
    main()
