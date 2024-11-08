
import requests
import streamlit as st

def fetch_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        quote = response.json()[0]
        return f"{quote['q']} — {quote['a']}"
    else:
        return "Unable to fetch quote."

st.title("Daily Inspirational Quotes")
if st.button("Get New Quote"):
    st.write(fetch_quote())
