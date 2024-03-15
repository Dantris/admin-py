import tkinter as tk
from tkinter import ttk

def on_submit():
    print("Submit clicked")

app = tk.Tk()
app.title("Admin Panel")

frame = ttk.Frame(app, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

welcome_label = ttk.Label(frame, text="Welcome to the Admin Panel")
welcome_label.pack()

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.pack()

app.mainloop()
