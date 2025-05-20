import pyttsx3 # type: ignore
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak_text():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Text field is empty!")
        return
    selected_voice = voice_var.get()
    engine.setProperty('voice', voices[0].id if selected_voice == 'Male' else voices[1].id)
    engine.setProperty('rate', int(speed_var.get()))
    engine.say(text)
    engine.runAndWait()

def clear_text():
    entry.delete(0, tk.END)

def save_audio():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Text field is empty!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        engine.save_to_file(text, file_path)
        engine.runAndWait()
        messagebox.showinfo("Saved", f"Audio saved to {file_path}")

def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entry.delete(0, tk.END)
            entry.insert(tk.END, content)

# Setup GUI
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

# Text input
tk.Label(root, text="Enter Text:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

# Voice selection
tk.Label(root, text="Select Voice:", bg="#f0f0f0").grid(row=1, column=0, padx=10, sticky="w")
voice_var = tk.StringVar(value='Male')
tk.Radiobutton(root, text="Male", variable=voice_var, value='Male', bg="#f0f0f0").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=voice_var, value='Female', bg="#f0f0f0").grid(row=1, column=1, padx=80, sticky="w")

# Speech rate
tk.Label(root, text="Speech Rate:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
speed_var = tk.StringVar(value='150')
tk.Entry(root, textvariable=speed_var, width=10).grid(row=2, column=1, sticky="w", padx=10)

# Buttons
tk.Button(root, text="Speak", command=speak_text, width=12).grid(row=3, column=0, pady=20)
tk.Button(root, text="Clear", command=clear_text, width=12).grid(row=3, column=1, sticky="w", padx=10)
tk.Button(root, text="Save as MP3", command=save_audio, width=12).grid(row=4, column=0)
tk.Button(root, text="Load Text File", command=load_text_file, width=12).grid(row=4, column=1, sticky="w", padx=10)

root.mainloop()
