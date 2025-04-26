import streamlit as st
from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("🧠 AI Text Summarizer")

text = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if text:
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")
