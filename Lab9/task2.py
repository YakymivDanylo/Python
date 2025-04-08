import tkinter as tk
from tkinter import filedialog, messagebox

class RingListApp:
    def __init__(self, master):
        self.master = master
        master.title("Гра Кільцевого Списку")

        self.filenames = []
        self.name_list = []
        self.excluded_names = []

        self.load_button = tk.Button(master, text="Завантажити прізвища з файлу", command=self.load_names)
        self.load_button.pack(pady=10)

        self.names_label = tk.Label(master, text="Завантажені прізвища:")
        self.names_label.pack()

        self.names_text = tk.Text(master, height=5, width=30, state=tk.DISABLED)
        self.names_text.pack()

        self.n_label = tk.Label(master, text="Введіть число n:")
        self.n_label.pack()
        self.n_entry = tk.Entry(master)
        self.n_entry.pack()

        self.start_name_label = tk.Label(master, text="Введіть прізвище для початку відліку:")
        self.start_name_label.pack()
        self.start_name_entry = tk.Entry(master)
        self.start_name_entry.pack()

        self.process_button = tk.Button(master, text="Розпочати обробку", command=self.process_list)
        self.process_button.pack(pady=10)

        self.excluded_label = tk.Label(master, text="Виключені прізвища:")
        self.excluded_label.pack()

        self.excluded_text = tk.Text(master, height=5, width=30, state=tk.DISABLED)
        self.excluded_text.pack()

        self.remaining_label = tk.Label(master, text="Залишився:")
        self.remaining_label.pack()
        self.remaining_result = tk.Label(master, text="")
        self.remaining_result.pack()

        self.save_button = tk.Button(master, text="Зберегти виключені прізвища у файл", command=self.save_excluded)
        self.save_button.pack(pady=10)

    def load_names(self):
        """Відкриває діалогове вікно для вибору файлу та зчитує з нього прізвища."""
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
        if file_path:
            self.filenames.append(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.name_list = [line.strip() for line in file if line.strip()]
                if len(self.name_list) != 20:
                    messagebox.showerror("Помилка", "Файл повинен містити рівно 20 прізвищ.")
                    self.name_list = []
                    self.names_text.config(state=tk.NORMAL)
                    self.names_text.delete(1.0, tk.END)
                    self.names_text.config(state=tk.DISABLED)
                    return
                self.display_names()
            except FileNotFoundError:
                messagebox.showerror("Помилка", "Файл не знайдено.")
            except Exception as e:
                messagebox.showerror("Помилка", f"Сталася помилка при зчитуванні файлу: {e}")

    def display_names(self):
        """Відображає завантажені прізвища в текстовому полі."""
        self.names_text.config(state=tk.NORMAL)
        self.names_text.delete(1.0, tk.END)
        for name in self.name_list:
            self.names_text.insert(tk.END, name + "\n")
        self.names_text.config(state=tk.DISABLED)

    def process_list(self):
        """Виконує обробку кільцевого списку згідно з введеними даними."""
        if not self.name_list:
            messagebox.showerror("Помилка", "Спочатку завантажте список прізвищ.")
            return

        try:
            n = int(self.n_entry.get())
            start_name = self.start_name_entry.get().strip()
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть ціле число для n.")
            return

        if not start_name:
            messagebox.showerror("Помилка", "Будь ласка, введіть прізвище для початку відліку.")
            return

        if start_name not in self.name_list:
            messagebox.showerror("Помилка", "Введене початкове прізвище не знайдено у списку.")
            return

        current_list = self.name_list[:]
        excluded = []
        current_index = current_list.index(start_name)

        while len(current_list) > 1:
            remove_index = (current_index + n - 1) % len(current_list)
            excluded_name = current_list.pop(remove_index)
            excluded.append(excluded_name)
            current_index = remove_index % len(current_list) if current_list else 0

        self.excluded_names = excluded
        self.display_results(current_list[0] if current_list else "")

    def display_results(self, remaining_name):
        """Відображає результати обробки (виключені прізвища та останнього учасника)."""
        self.excluded_text.config(state=tk.NORMAL)
        self.excluded_text.delete(1.0, tk.END)
        for name in self.excluded_names:
            self.excluded_text.insert(tk.END, name + "\n")
        self.excluded_text.config(state=tk.DISABLED)

        self.remaining_result.config(text=remaining_name)

    def save_excluded(self):
        """Зберігає список виключених прізвищ у текстовий файл."""
        if not self.excluded_names:
            messagebox.showinfo("Інформація", "Немає виключених прізвищ для збереження.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    for name in self.excluded_names:
                        file.write(name + "\n")
                messagebox.showinfo("Успіх", "Список виключених прізвищ збережено.")
            except Exception as e:
                messagebox.showerror("Помилка", f"Сталася помилка при збереженні файлу: {e}")

root = tk.Tk()
app = RingListApp(root)
root.mainloop()