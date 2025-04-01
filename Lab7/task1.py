import tkinter as tk
from tkinter import ttk
import datetime

def calculate_anniversary_dates():
    """Обчислює ювілейні дати на основі дати народження."""
    birthdate_str = birthdate_entry.get()
    try:
        birthdate = datetime.datetime.strptime(birthdate_str, "%d%m%Y").date()
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Неправильний формат дати (ДДММРРРР)")
        return

    result_text.delete(1.0, tk.END)
    for year in range(birthdate.year, birthdate.year + 101):
        if (year - birthdate.year) % 5 == 0:
            anniversary_date = birthdate.replace(year=year)
            day_of_week = anniversary_date.strftime("%A")
            result_text.insert(tk.END, f"{anniversary_date.strftime('%d.%m.%Y')} ({day_of_week})\n")


window = tk.Tk()
window.title("Розрахунок ювілейних дат")


birthdate_label = ttk.Label(window, text="Дата народження (ДДММРРРР):")
birthdate_label.pack()
birthdate_entry = ttk.Entry(window)
birthdate_entry.pack()


calculate_button = ttk.Button(window, text="Розрахувати", command=calculate_anniversary_dates)
calculate_button.pack()


result_text = tk.Text(window, height=10, width=40)
result_text.pack()

window.mainloop()