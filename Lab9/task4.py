import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class SchoolTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = TreeNode(data)
                return
            elif not current.right:
                current.right = TreeNode(data)
                return
            queue.append(current.left)
            queue.append(current.right)

    def delete(self, data):
        if not self.root:
            return False

        # Знаходимо вузол для видалення та його батька
        node_to_delete = None
        parent = None
        queue = deque([(self.root, None)])
        while queue:
            current, par = queue.popleft()
            if current.data == data:
                node_to_delete = current
                parent = par
                break
            if current.left:
                queue.append((current.left, current))
            if current.right:
                queue.append((current.right, current))

        if not node_to_delete:
            return False

        # Випадок 1: Вузол - лист
        if not node_to_delete.left and not node_to_delete.right:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
            return True

        # Випадок 2: Вузол має одну дитину
        if not node_to_delete.left:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.right
                else:
                    parent.right = node_to_delete.right
            else:
                self.root = node_to_delete.right
            return True
        elif not node_to_delete.right:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.left
                else:
                    parent.right = node_to_delete.left
            else:
                self.root = node_to_delete.left
            return True

        # Випадок 3: Вузол має двох дітей
        # Знаходимо найлівіший вузол у правому піддереві (наступник)
        successor = node_to_delete.right
        successor_parent = node_to_delete
        while successor.left:
            successor_parent = successor
            successor = successor.left

        node_to_delete.data = successor.data
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
        return True

    def bfs(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if not node:
            return "Не знайдено"
        if node.data == data:
            return "Знайдено"
        left_result = self._search_recursive(node.left, data)
        if left_result == "Знайдено":
            return "Знайдено"
        right_result = self._search_recursive(node.right, data)
        return right_result

    def _get_tree_string(self, node, level=0, prefix=""):
        if not node:
            return ""
        indent = "    " * level
        return f"{indent}{prefix}{node.data}\n" + \
               self._get_tree_string(node.left, level + 1, "L: ") + \
               self._get_tree_string(node.right, level + 1, "R: ")

    def get_tree_representation(self):
        return self._get_tree_string(self.root)

class SchoolApp:
    def __init__(self, master):
        self.master = master
        master.title("Керування навчальними закладами")

        self.school_tree = SchoolTree()

        # Додавання
        self.add_label = ttk.Label(master, text="Додати заклад:")
        self.add_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.add_entry = ttk.Entry(master)
        self.add_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.add_button = ttk.Button(master, text="Додати", command=self.add_school)
        self.add_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Видалення
        self.delete_label = ttk.Label(master, text="Видалити заклад:")
        self.delete_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.delete_entry = ttk.Entry(master)
        self.delete_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.delete_button = ttk.Button(master, text="Видалити", command=self.delete_school)
        self.delete_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        # Обхід
        self.bfs_button = ttk.Button(master, text="Обхід дерева (BFS)", command=self.perform_bfs)
        self.bfs_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        self.bfs_result_label = ttk.Label(master, text="Результат обходу:")
        self.bfs_result_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.bfs_result_text = tk.Text(master, height=5, width=40)
        self.bfs_result_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

        # Пошук
        self.search_label = ttk.Label(master, text="Пошук за назвою:")
        self.search_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.search_entry = ttk.Entry(master)
        self.search_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        self.search_button = ttk.Button(master, text="Пошук", command=self.search_school)
        self.search_button.grid(row=5, column=2, padx=5, pady=5, sticky="ew")
        self.search_result_label = ttk.Label(master, text="Результат пошуку:")
        self.search_result_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="w")
        self.search_result_display = ttk.Label(master, text="")
        self.search_result_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Відображення дерева
        self.tree_label = ttk.Label(master, text="Стан дерева:")
        self.tree_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.tree_text = tk.Text(master, height=10, width=40)
        self.tree_text.grid(row=9, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        self.update_tree_display()

        master.grid_columnconfigure(1, weight=1)

    def add_school(self):
        school_name = self.add_entry.get()
        if school_name:
            self.school_tree.insert(school_name)
            self.add_entry.delete(0, tk.END)
            self.update_tree_display()
        else:
            messagebox.showerror("Помилка", "Будь ласка, введіть назву навчального закладу.")

    def delete_school(self):
        school_name = self.delete_entry.get()
        if school_name:
            if self.school_tree.delete(school_name):
                self.delete_entry.delete(0, tk.END)
                self.update_tree_display()
            else:
                messagebox.showerror("Помилка", f"Заклад '{school_name}' не знайдено в дереві.")
        else:
            messagebox.showerror("Помилка", "Будь ласка, введіть назву навчального закладу для видалення.")

    def perform_bfs(self):
        bfs_result = self.school_tree.bfs()
        self.bfs_result_text.delete("1.0", tk.END)
        self.bfs_result_text.insert(tk.END, ", ".join(bfs_result))

    def search_school(self):
        search_term = self.search_entry.get()
        if search_term:
            result = self.school_tree.search(search_term)
            self.search_result_display.config(text=result)
        else:
            messagebox.showerror("Помилка", "Будь ласка, введіть назву для пошуку.")

    def update_tree_display(self):
        self.tree_text.delete("1.0", tk.END)
        self.tree_text.insert(tk.END, self.school_tree.get_tree_representation())

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolApp(root)
    root.mainloop()