import tkinter as tk
from tkinter import ttk, messagebox
from collections import namedtuple
import random

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Облік студентів та стипендії")

        self.Student = namedtuple("Student", ["прізвище", "середній_бал", "спеціальність", "курс"])
        self.student_entries = []

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        for i in range(7):
            frame = ttk.Frame(self.notebook)
            self.create_student_input_fields(frame, i + 1)
            self.notebook.add(frame, text=f'Студент {i + 1}')

        self.process_button = ttk.Button(root, text="Обчислити стипендії", command=self.process_students)
        self.process_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def create_student_input_fields(self, parent_frame, student_number):
        labels = ["Прізвище:", "Середній бал:", "Спеціальність:", "Курс:"]
        student_entries = {}
        for i, label_text in enumerate(labels):
            label = ttk.Label(parent_frame, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(parent_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            student_entries[labels[i][:-1].lower().replace(' ', '_')] = entry
        self.student_entries.append(student_entries)

    def get_student_data_from_gui(self):
        students = []
        for entry_set in self.student_entries:
            try:
                прізвище = entry_set['прізвище'].get()
                середній_бал = float(entry_set['середній_бал'].get())
                спеціальність = entry_set['спеціальність'].get()
                курс = int(entry_set['курс'].get())
                students.append(self.Student(прізвище, середній_бал, спеціальність, курс))
            except ValueError:
                messagebox.showerror("Помилка введення", "Будь ласка, введіть коректні числові значення для середнього балу та курсу.")
                return None
        return tuple(students)

    def bursary(self, students):
        if not students:
            return "Немає даних про студентів."

        total_score = sum(student.середній_бал for student in students)
        average_score = total_score / len(students) if students else 0

        non_bursary_students = [student.прізвище for student in students if student.середній_бал <= average_score]

        message = f"Середній бал по всім студентам: {average_score:.2f}\n"
        if non_bursary_students:
            message += f"Студенти {', '.join(non_bursary_students)} не будуть отримувати стипендію."
        else:
            message += "Усі студенти отримуватимуть стипендію."
        return message

    def process_students(self):
        students_tuple = self.get_student_data_from_gui()
        if students_tuple:
            result_first = self.bursary(students_tuple)
            messagebox.showinfo("Результат (перший раз)", result_first)

            updated_students = []
            for student in students_tuple:
                new_average_score = round(random.uniform(1.0, 5.0), 2)
                updated_students.append(student._replace(середній_бал=new_average_score))
            updated_students_tuple = tuple(updated_students)

            result_second = self.bursary(updated_students_tuple)
            messagebox.showinfo("Результат (після оновлення)", result_second)

def main():
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()