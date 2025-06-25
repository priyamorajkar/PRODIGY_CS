import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

def process_text():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return

    mode = var_mode.get()
    if not message:
        messagebox.showerror("Input Error", "Please enter a message.")
        return

    result = caesar_cipher(message, shift, mode)
    result_label.config(text=f"Result: {result}")

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher Home")
window.geometry("600x400")
window.config(bg="green")  # Soft blue background

# Center frame on the background
main_frame = tk.Frame(window, bg="#ffffff", bd=2, relief="ridge")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(main_frame, text="Caesar Cipher Tool", font=("Arial", 16, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

# Message Entry
tk.Label(main_frame, text="Enter your message:", bg="#ffffff", fg="#333").pack()
entry_message = tk.Entry(main_frame, width=50)
entry_message.pack(pady=5)

# Shift Entry
tk.Label(main_frame, text="Enter shift value:", bg="#ffffff", fg="#333").pack()
entry_shift = tk.Entry(main_frame, width=10)
entry_shift.pack(pady=5)

# Mode selection
tk.Label(main_frame, text="Choose mode:", bg="#ffffff", fg="#333").pack()
var_mode = tk.StringVar(value="encrypt")
tk.Radiobutton(main_frame, text="Encrypt", variable=var_mode, value="encrypt", bg="#ffffff").pack()
tk.Radiobutton(main_frame, text="Decrypt", variable=var_mode, value="decrypt", bg="#ffffff").pack()

# Process Button
tk.Button(main_frame, text="Process", command=process_text, bg="#007ACC", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

# Result
result_label = tk.Label(main_frame, text="Result: ", bg="#ffffff", fg="#000000", wraplength=400)
result_label.pack(pady=(0, 10))

# Run the GUI
window.mainloop()
