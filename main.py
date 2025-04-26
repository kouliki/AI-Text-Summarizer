pip install transformers
pip install PyPDF2

from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample long text
long_text = """
Artificial Intelligence is a field of computer science that enables machines to mimic human intelligence.
It involves learning, reasoning, problem-solving, perception, and language understanding. Over the last decade,
AI has evolved rapidly with applications ranging from natural language processing to autonomous vehicles.
With increased computational power and access to big data, AI systems are now able to outperform humans in many tasks.
"""

# Perform summarization
summary = summarizer(long_text, max_length=80, min_length=30, do_sample=False)
print("Summary:")
print(summary[0]['summary_text'])

import PyPDF2
from google.colab import files

uploaded = files.upload()  # Upload your PDF

for fn in uploaded.keys():
    with open(fn, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text()

summary = summarizer(full_text, max_length=150, min_length=40, do_sample=False)
print("PDF Summary:")
print(summary[0]['summary_text'])
