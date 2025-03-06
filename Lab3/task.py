import tkinter as tk
from tkinter import messagebox
import re

def find_barcodes():
    text = txt_input.get("1.0", "end-1c")
    barcode_pattern = r'\b\d{13}\b'
    barcodes = re.findall(barcode_pattern, text)
    txt_result.delete("1.0", "end")

    if barcodes:
        txt_result.insert("1.0", "\n".join(barcodes))
        lbl_count.config(text=f"Кількість штрих-кодів: {len(barcodes)}")
    else:
        messagebox.showinfo("Результат", "Штрих-коди не знайдено.")

#
def extract_barcode():
    barcode_to_extract = txt_extract.get()
    text = txt_input.get("1.0", "end-1c")


    barcode_pattern = r'\b' + re.escape(barcode_to_extract) + r'\b'
    matches = re.findall(barcode_pattern, text)

    if matches:
        messagebox.showinfo("Вилучення", f"Знайдений штрих-код: {matches[0]}")
    else:
        messagebox.showerror("Помилка", "Штрих-код не знайдений.")


def replace_barcode():
    old_barcode = txt_replace_old.get()
    new_barcode = txt_replace_new.get()
    text = txt_input.get("1.0", "end-1c")


    barcode_pattern = r'\b' + re.escape(old_barcode) + r'\b'
    if re.search(barcode_pattern, text):
        text = re.sub(barcode_pattern, new_barcode, text)
        txt_input.delete("1.0", "end")
        txt_input.insert("1.0", text)
        messagebox.showinfo("Замінено", f"Штрих-код {old_barcode} замінено на {new_barcode}")
    else:
        messagebox.showerror("Помилка", f"Штрих-код {old_barcode} не знайдений для заміни.")


root = tk.Tk()
root.title("Аналізатор штрих-кодів")


txt_input = tk.Text(root, height=10, width=40)
txt_input.pack(padx=10, pady=10)

btn_find = tk.Button(root, text="Знайти штрих-коди", command=find_barcodes)
btn_find.pack(padx=10, pady=5)

lbl_count = tk.Label(root, text="Кількість штрих-кодів: 0")
lbl_count.pack(padx=10, pady=5)

txt_result = tk.Text(root, height=5, width=40)
txt_result.pack(padx=10, pady=10)

txt_extract = tk.Entry(root, width=40)
txt_extract.pack(padx=10, pady=5)

btn_extract = tk.Button(root, text="Вилучити штрих-код", command=extract_barcode)
btn_extract.pack(padx=10, pady=5)

txt_replace_old = tk.Entry(root, width=40)
txt_replace_old.pack(padx=10, pady=5)
txt_replace_new = tk.Entry(root, width=40)
txt_replace_new.pack(padx=10, pady=5)

btn_replace = tk.Button(root, text="Заміна штрих-коду", command=replace_barcode)
btn_replace.pack(padx=10, pady=5)

root.mainloop()
