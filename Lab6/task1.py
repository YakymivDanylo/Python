import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
from datetime import datetime


# Абстрактний клас Програмний продукт
class SoftwareProduct(ABC):
    def __init__(self, name, developer, release_date, price, sold_date=None):
        self.name = name
        self.developer = developer
        self.release_date = release_date
        self.price = price
        self.sold_date = sold_date

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def is_sold_on(self, date):
        return self.sold_date == date


# Похідний клас Операційна система
class OperatingSystem(SoftwareProduct):
    def __init__(self, name, developer, release_date, price, kernel_type, sold_date=None):
        super().__init__(name, developer, release_date, price, sold_date)
        self.kernel_type = kernel_type

    def get_type(self):
        return "Операційна система"

    def get_info(self):
        return f"{self.get_type()}: {self.name}, {self.developer}, {self.release_date}, {self.price}$, Kernel: {self.kernel_type}, Sold: {self.sold_date}"


# Похідний клас Інформаційна система
class InformationSystem(SoftwareProduct):
    def __init__(self, name, developer, release_date, price, industry, sold_date=None):
        super().__init__(name, developer, release_date, price, sold_date)
        self.industry = industry

    def get_type(self):
        return "Інформаційна система"

    def get_info(self):
        return f"{self.get_type()}: {self.name}, {self.developer}, {self.release_date}, {self.price}$, Industry: {self.industry}, Sold: {self.sold_date}"


# Головне вікно
class SoftwareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Програмне забезпечення")

        self.software_list = [
            OperatingSystem("Windows 11", "Microsoft", "2021-10-05", 150, "Hybrid", "2024-01-10"),
            InformationSystem("SAP ERP", "SAP", "2015-06-20", 5000, "Enterprise", "2024-02-15"),
            OperatingSystem("Ubuntu 22.04", "Canonical", "2022-04-21", 0, "Linux", None)
        ]

        ttk.Label(root, text="Перелік програмного забезпечення:").pack()
        self.listbox = tk.Listbox(root, width=80, height=10)
        self.listbox.pack()
        self.update_listbox()

        ttk.Label(root, text="Дата продажу (YYYY-MM-DD):").pack()
        self.date_entry = ttk.Entry(root)
        self.date_entry.pack()
        ttk.Button(root, text="Пошук", command=self.search_by_date).pack()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for software in self.software_list:
            self.listbox.insert(tk.END, software.get_info())

    def search_by_date(self):
        search_date = self.date_entry.get()
        try:
            datetime.strptime(search_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Помилка", "Невірний формат дати!")
            return

        results = [s.get_info() for s in self.software_list if s.is_sold_on(search_date)]

        if results:
            messagebox.showinfo("Результати пошуку", "\n".join(results))
        else:
            messagebox.showinfo("Результати пошуку", "Жодного збігу не знайдено.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareApp(root)
    root.mainloop()
