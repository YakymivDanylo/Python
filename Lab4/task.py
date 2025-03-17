import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string


# Функція для створення файлу TF_1 з розділовими знаками
def create_file_tf1():
    words = ["".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) for _ in range(100)]
    punctuations = [",", ".", "!", "?"]  # Розділові знаки
    sentences = []

    for _ in range(10):
        sentence_length = random.randint(5, 15)
        sentence = " ".join(random.sample(words, sentence_length))
        sentence = sentence.capitalize() + random.choice(punctuations)  # Кожне речення починається з великої літери
        sentences.append(sentence)

    with open("TF_1.txt", "w") as file:
        file.write("\n".join(sentences))

    messagebox.showinfo("Info", "Файл TF_1 створено з розділовими знаками.")


# Функція для знаходження найдовших слів
def find_longest_words():
    try:
        with open("TF_1.txt", "r") as file:
            text = file.read()

        words = text.split()
        max_length = max(len(word.strip(",.!?")) for word in words)  # Видаляти розділові знаки перед порівнянням
        longest_words = [word.strip(",.!?") for word in words if len(word.strip(",.!?")) == max_length]

        with open("TF_2.txt", "w") as file:
            file.write(" ".join(longest_words))

        messagebox.showinfo("Info", "Найдовші слова записані в TF_2.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Файл TF_1 не знайдено!")


# Функція для виведення вмісту TF_2 по 5 слів у рядку
def display_tf2():
    try:
        with open("TF_2.txt", "r") as file:
            words = file.read().split()

        output = ""
        for i in range(0, len(words), 5):
            output += " ".join(words[i:i + 5]) + "\n"

        messagebox.showinfo("Info", output)
    except FileNotFoundError:
        messagebox.showerror("Error", "Файл TF_2 не знайдено!")


# GUI
def main():
    root = tk.Tk()
    root.title("Text File Processor")

    tk.Button(root, text="Створити файл TF_1", command=create_file_tf1).pack(pady=10)
    tk.Button(root, text="Знайти найдовші слова", command=find_longest_words).pack(pady=10)
    tk.Button(root, text="Вивести вміст TF_2", command=display_tf2).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
