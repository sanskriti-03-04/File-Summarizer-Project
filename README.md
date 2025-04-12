#File-Summarizer-Project
This Web App allows users to upload files such as .log .txt .pdf and .docx for extraction and summarization. The model is built with NLP ( Natural Language Processing ) 
#What are NLP's ?
NLP is a machine learnign technology that gives computers the ability to interpret, manipulate, and comprehend human language. Organizations today have large volumes of voice and text data from various communication channels like emails, text messages, social media newsfeeds, video, audio, and more. [Click here for more resources](https://aws.amazon.com/what-is/nlp/#:~:text=Natural%20language%20processing%20(NLP)%20combines,models%20to%20process%20human%20language.&text=Computational%20linguistics%20is%20the%20science,with%20computers%20and%20software%20tools.)
#Dependencies 
Here is a list of all the dependencies used in this project 
streamlit
pandas
transformers
torch
PyMuPDF
python-docx 
#Installation 
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
