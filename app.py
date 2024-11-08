# from textblob import TextBlob

# def analyze_sentiment(text):
#     """
#     Analyze the sentiment of the given text using TextBlob.
#     Returns a sentiment label based on the polarity score.
#     """
#     blob = TextBlob(text)
#     # Polarity is a float between -1.0 (negative) and 1.0 (positive)
#     polarity = blob.sentiment.polarity

#     if polarity > 0:
#         return "Positive 😊"
#     elif polarity < 0:
#         return "Negative 😞"
#     else:
#         return "Neutral 😐"

# if __name__ == "__main__":
#     print("Welcome to the Sentiment Analyzer!")
#     user_text = input("Enter a sentence to analyze its sentiment: ")
#     result = analyze_sentiment(user_text)
#     print(f"Sentiment: {result}")


import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using TextBlob.
    Returns a sentiment label based on the polarity score.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Streamlit App UI
st.title("Minimalist Sentiment Analyzer")
st.write("Enter a sentence to analyze its sentiment.")

# Text input field
user_input = st.text_input("Your sentence:")

if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_result = analyze_sentiment(user_input)
        st.write(f"**Sentiment:** {sentiment_result}")
    else:
        st.write("Please enter text to analyze.")
