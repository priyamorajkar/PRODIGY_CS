import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Encryption key
KEY = 123  # You can make this input based

def encrypt_decrypt_image(file_path, mode):
    try:
        image = Image.open(file_path)
        image = image.convert('RGB')
        pixels = image.load()

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r, g, b = pixels[i, j]
                if mode == 'encrypt':
                    pixels[i, j] = (r ^ KEY, g ^ KEY, b ^ KEY)
                else:
                    pixels[i, j] = (r ^ KEY, g ^ KEY, b ^ KEY)

        # Save the image
        base, ext = os.path.splitext(file_path)
        new_file = base + ('_encrypted.png' if mode == 'encrypt' else '_decrypted.png')
        image.save(new_file)
        messagebox.showinfo("Success", f"Image {mode}ed successfully!\nSaved as: {new_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_file(mode):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        encrypt_decrypt_image(file_path, mode)

# GUI Setup
root = tk.Tk()
root.title("Simple Image Encryption Tool")
root.geometry("400x200")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="Image Encryption & Decryption Tool", font=("Helvetica", 16), bg="#f0f0f0")
title.pack(pady=20)

encrypt_btn = tk.Button(root, text="Encrypt Image", width=20, command=lambda: open_file('encrypt'))
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt Image", width=20, command=lambda: open_file('decrypt'))
decrypt_btn.pack(pady=10)

root.mainloop()
