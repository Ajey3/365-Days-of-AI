# daily_quotes.py
# Day 3: Daily Inspirational Quotes App
# This application displays an inspirational quote daily, fetched from an online API.

import tkinter as tk
import requests

def get_quote():
    """Fetch a random inspirational quote from the Zen Quotes API."""
    try:
        response = requests.get("https://zenquotes.io/api/random")
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract the quote and author
            quote = data[0]['q']
            author = data[0]['a']
            quote_label.config(text=f'"{quote}"\n\n- {author}')
        else:
            quote_label.config(text="Could not fetch a quote at this time.")
    except requests.exceptions.RequestException as e:
        # If there is a network error
        quote_label.config(text="Network error. Please try again later.")

# Set up the main application window
window = tk.Tk()
window.title("Daily Inspirational Quote")
window.geometry("400x300")
window.configure(bg="white")

# App heading
heading_label = tk.Label(window, text="Inspirational Quote of the Day", font=("Helvetica", 16, "bold"), bg="white")
heading_label.pack(pady=10)

# Label to display the quote
quote_label = tk.Label(window, text="Click below to get your quote!", wraplength=350, font=("Helvetica", 12), bg="white", justify="center")
quote_label.pack(pady=20)

# Button to fetch a new quote
quote_button = tk.Button(window, text="Get New Quote", command=get_quote, bg="lightblue", font=("Helvetica", 12))
quote_button.pack(pady=10)

# Run the main event loop
window.mainloop()
