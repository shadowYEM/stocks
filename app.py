import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load sentiment analysis model and tokenizer
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define function to perform sentiment analysis on input text
def analyze_sentiment(input_text):
    classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    result = classifier(input_text)
    return result[0]

# Define Streamlit app
def app():
    st.title("Sentiment Analysis App")
    input_text = st.text_input("Enter text to analyze:")
    if input_text:
        result = analyze_sentiment(input_text)
        st.write(f"Sentiment: {result['label']}")
        st.write(f"Score: {result['score']}")

