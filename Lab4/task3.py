import tkinter as tk
from tkinter import messagebox
import logging
import os

# Configure logging
logging.basicConfig(filename='session_log.txt', level=logging.INFO)


# Function to create files if they do not exist
def create_files():
    if not os.path.exists('input_data.txt'):
        with open('input_data.txt', 'w') as file:
            file.write("5 3")  # Example initial data for calculations
    if not os.path.exists('output_data.txt'):
        with open('output_data.txt', 'w') as file:
            pass  # File created empty
    if not os.path.exists('session_log.txt'):
        with open('session_log.txt', 'w') as file:
            pass  # File created empty


# Function to write input data to the file
def write_input_data(num1, num2):
    try:
        with open('input_data.txt', 'w') as file:
            file.write(f"{num1} {num2}")  # Write two numbers to the file
        logging.info("Input data written to input_data.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write input data: {e}")


# Function to import input data from file
def import_data():
    try:
        with open('input_data.txt', 'r') as file:
            data = file.read().strip()
            if not data:
                raise ValueError("File is empty, please enter data")
            num1, num2 = map(float, data.split())
            entry_num1.delete(0, tk.END)
            entry_num1.insert(0, str(num1))
            entry_num2.delete(0, tk.END)
            entry_num2.insert(0, str(num2))
            logging.info("Action 2: 'Import input data' selected")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Function to calculate the expression
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by 0 is forbidden")
            result = num1 / num2
        elif operation == "^":
            result = num1 ** num2

        result_var.set(f"Result: {result}")
        logging.info("Action 4: 'Calculate expression' selected")

        # Write result to the output file
        with open('output_data.txt', 'w') as file:
            file.write(f"{num1} {operation} {num2}, Result: {result}")
        logging.info("Action 7: 'Export result to file' selected")

    except ValueError:
        messagebox.showerror("Error", "Invalid input values")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))


# Create main window
root = tk.Tk()
root.title("Arithmetic Calculator")

# Create files on startup
create_files()

# Input fields
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Select operation
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/", "^"]
for i, op in enumerate(operations):
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).grid(row=2, column=i)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=3)

# Buttons
tk.Button(root, text="Import input data", command=import_data).grid(row=4, column=0)
tk.Button(root, text="Calculate expression", command=calculate).grid(row=4, column=1)
tk.Button(root, text="Export result to file",
          command=lambda: logging.info("Action 7: 'Export result to file' selected")).grid(row=4, column=2)


# Close program function
def close_program():
    logging.info("Action 8: Application closed")
    root.quit()


root.protocol("WM_DELETE_WINDOW", close_program)

# Start the application
logging.info("Action 1: Application started")
root.mainloop()
