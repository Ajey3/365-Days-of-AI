import random
import tkinter as tk
from tkinter import messagebox

def generate_random_number():
    """Generate a random number between the user-defined range."""
    try:
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())
        if min_val >= max_val:
            messagebox.showerror("Input Error", "Minimum should be less than maximum.")
            return
        random_number = random.randint(min_val, max_val)
        result_label.config(text=f"Random Number: {random_number}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

# Set up the UI window
window = tk.Tk()
window.title("Random Number Generator")
window.geometry("300x200")
window.configure(bg="white")

# UI elements
tk.Label(window, text="Enter Minimum Value:", bg="white").pack(pady=5)
min_entry = tk.Entry(window)
min_entry.pack(pady=5)

tk.Label(window, text="Enter Maximum Value:", bg="white").pack(pady=5)
max_entry = tk.Entry(window)
max_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate", command=generate_random_number, bg="black", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", bg="white", font=("Helvetica", 12, "bold"))
result_label.pack(pady=5)

# Start the main loop
window.mainloop()
