import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Adjust the path based on your installation

def process_image():
    file_path = file_var.get()
    if file_path:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang='eng')
        save_to_file(text)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "OCR output saved to 'output.txt'")
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select an image.")
        result_text.config(state=tk.DISABLED)

def browse_file():
    file_path = filedialog.askopenfilename()
    file_var.set(file_path)

def save_to_file(text):
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(text)

app = tk.Tk()
app.title("Image Text Extractor")

# Create and place widgets in the window
file_var = tk.StringVar()

file_label = tk.Label(app, text="Select an image:")
file_label.pack(pady=10)

file_entry = tk.Entry(app, textvariable=file_var, state='disabled', width=60)
file_entry.pack(pady=10)

file_button = tk.Button(app, text="Browse Image", command=browse_file)
file_button.pack(pady=10)

process_button = tk.Button(app, text="Process Image", command=process_image)
process_button.pack(pady=10)

result_text = tk.Text(app, height=2, width=50, state=tk.DISABLED)
result_text.pack(pady=10)

app.mainloop()