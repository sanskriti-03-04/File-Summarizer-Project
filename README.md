##File-Summarizer-Project
This Web App allows users to upload files such as .log .txt .pdf and .docx for extraction and summarization. The model is built with NLP ( Natural Language Processing ) 
##Dependencies 
Here is a list of all the dependencies used in this project 
streamlit
pandas
transformers
torch
PyMuPDF
python-docx 
##Installation 
Step 1 : Clone the repository 
git clone https://github.com/sanskriti03-04/File-Summarizer-Project.git
cd log-text-summarizer
Step 2 : Create a virtual environment 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate 
Step 3 : Install dependencies 
pip install -r requirements.txt
Step 4 : Run the app 
streamlit run main.py
#Library/Tool
1) Web App UI	-> Streamlit
2) Summarization	-> HuggingFace Transformers
3) File Handling	->PyMuPDF, python-docx, pandas
4) Model Used	-> facebook/bart-large-cnn (or distilbart)
5) Deployment	-> Streamlit Cloud / Render
