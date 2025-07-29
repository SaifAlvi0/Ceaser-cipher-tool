
import tkinter as tk
from tkinter import messagebox, simpledialog

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
            else:  # decrypt
                shifted_char = chr((ord(char) - base - shift) % 26 + base)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def run_caesar():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Enter text first!")
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number!")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool (Kali Linux)")
root.geometry("500x400")

# Text Input
tk.Label(root, text="Enter Text:").pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# Shift Input
tk.Label(root, text="Shift Value (0-25):").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Mode Selection (Encrypt/Decrypt)
mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").pack()

# Process Button
tk.Button(root, text="Run Caesar Cipher", command=run_caesar).pack()

# Result Display
tk.Label(root, text="Result:").pack()
result_text = tk.Text(root, height=5, width=50)
result_text.pack()

root.mainloop()
