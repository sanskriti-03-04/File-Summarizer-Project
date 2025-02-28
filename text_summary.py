import streamlit as st
import pandas as pd
from transformers import pipeline
import fitz  # PyMuPDF for PDF extraction
import docx  # python-docx for DOCX extraction
from io import BytesIO

# Function to process log files
def process_log_file(uploaded_file):
    log_data = []
    for line in uploaded_file:
        decoded_line = line.decode("utf-8").strip()
        if "ERROR" in decoded_line:
            log_data.append((decoded_line, "ERROR"))
        elif "WARNING" in decoded_line:
            log_data.append((decoded_line, "WARNING"))
        else:
            log_data.append((decoded_line, "INFO"))
    
    return pd.DataFrame(log_data, columns=["Log Message", "Category"])

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to summarize text
def summarize_text(text, max_length=150, min_length=50):
    if not text.strip():
        return "No valid text found for summarization."

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Ensure text fits within model limits
    max_input_length = 1024  # Token limit for the model
    chunk_size = max_input_length  # Ensure each chunk fits the model
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)] 
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
        summaries.append(summary)

    return " ".join(summaries)  # Merge summaries for final output


# Streamlit App
st.set_page_config(page_title="Log & Text Summarizer", layout="wide")
st.title("🔍 Log & Document Analyzer & Summarizer")
st.write("Upload a `.log`, `.txt`, `.pdf`, or `.docx` file to analyze system logs or summarize text.")

uploaded_file = st.file_uploader("Upload File", type=["log", "txt", "pdf", "docx"])
text = ""

if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1]
    if file_extension in ["log", "txt"]:
        logs_df = process_log_file(uploaded_file)
        st.write("### Parsed Log Data")
        st.dataframe(logs_df)
        if st.button("Summarize Errors & Warnings"):
            summary = summarize_text("\n".join(logs_df[logs_df['Category'].isin(["ERROR", "WARNING"])] ["Log Message"].tolist()))
            st.write("### 🚀 Summary of Critical Logs:")
            st.write(summary)
    elif file_extension == "pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == "docx":
        text = extract_text_from_docx(uploaded_file)

if text:
    st.write("### Extracted Text")
    st.text_area("Extracted Content", text, height=300)
    if st.button("Summarize Document"):
        summary = summarize_text(text)
        st.write("### ✨ Summary:")
        st.write(summary)

