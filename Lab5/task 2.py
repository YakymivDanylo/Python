import tkinter as tk
from tkinter import messagebox


class EducationalInstitution:
    def __init__(self, name="", location="", students=0):
        self.name = name
        self.location = location
        self.students = students

    def show(self):
        return f"Заклад: {self.name}, Місце: {self.location}, Студенти: {self.students}"

    def __del__(self):
        print("Лабораторна робота виконана студентом 2 курсу ПІБ студента")


class University(EducationalInstitution):
    def __init__(self, name="", location="", students=0, ranking=1):
        super().__init__(name, location, students)
        self.ranking = ranking

    def show(self):
        return f"Заклад: {self.name}, Місце: {self.location}, Студенти: {self.students}, Рейтинг: {self.ranking}"


class School(EducationalInstitution):
    def __init__(self, name="", location="", students=0, level="Середня"):
        super().__init__(name, location, students)
        self.level = level

    def show(self):
        return f"Заклад: {self.name}, Місце: {self.location}, Студенти: {self.students}, Рівень: {self.level}"


class HigherEducationInstitution(EducationalInstitution):
    def __init__(self, name="", location="", students=0, accreditation="III-IV"):
        super().__init__(name, location, students)
        self.accreditation = accreditation

    def show(self):
        return f"Заклад: {self.name}, Місце: {self.location}, Студенти: {self.students}, Акредитація: {self.accreditation}"


class Faculty(EducationalInstitution):
    def __init__(self, name="", location="", students=0, specialization="Інженерія"):
        super().__init__(name, location, students)
        self.specialization = specialization

    def show(self):
        return f"Заклад: {self.name}, Місце: {self.location}, Студенти: {self.students}, Спеціалізація: {self.specialization}"


# GUI додаток
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Навчальні заклади")

        tk.Label(root, text="Назва закладу:").grid(row=0, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)

        tk.Label(root, text="Місце розташування:").grid(row=1, column=0)
        self.entry_location = tk.Entry(root)
        self.entry_location.grid(row=1, column=1)

        tk.Label(root, text="Кількість студентів:").grid(row=2, column=0)
        self.entry_students = tk.Entry(root)
        self.entry_students.grid(row=2, column=1)

        tk.Label(root, text="Тип закладу:").grid(row=3, column=0)
        self.var_type = tk.StringVar()
        self.var_type.set("Університет")
        self.option_type = tk.OptionMenu(root, self.var_type, "Університет", "Школа", "Факультет",
                                         "Заклад вищої освіти")
        self.option_type.grid(row=3, column=1)

        self.object = None  # Змінна для збереження об'єкта

        tk.Button(root, text="Зберегти", command=self.create_object).grid(row=4, column=0)
        tk.Button(root, text="Показати", command=self.show_info).grid(row=4, column=1)
        tk.Button(root, text="Видалити об'єкт", command=self.delete_object).grid(row=5, column=0, columnspan=2)

    def create_object(self):
        name = self.entry_name.get()
        location = self.entry_location.get()
        students = int(self.entry_students.get() or 0)
        obj_type = self.var_type.get()

        if obj_type == "Університет":
            self.object = University(name, location, students)
        elif obj_type == "Школа":
            self.object = School(name, location, students)
        elif obj_type == "Факультет":
            self.object = Faculty(name, location, students)
        elif obj_type == "Заклад вищої освіти":
            self.object = HigherEducationInstitution(name, location, students)

        messagebox.showinfo("Статус", "Об'єкт створено!")

    def show_info(self):
        if self.object:
            messagebox.showinfo("Інформація", self.object.show())
        else:
            messagebox.showwarning("Помилка", "Об'єкт ще не створено!")

    def delete_object(self):
        if self.object:
            del self.object
            self.object = None
            messagebox.showinfo("Статус", "Об'єкт видалено!")
        else:
            messagebox.showwarning("Помилка", "Об'єкт ще не створено!")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
