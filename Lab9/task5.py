import tkinter as tk
from tkinter import ttk

class GraphRepresentationApp:
    def __init__(self, master):
        self.master = master
        master.title("Представлення Заданого Графу")

        self.edges = [
            ('e', 'e'),
            ('e', 'a'),
            ('e', 'b'),
            ('e', 'f'),
            ('a', 'd'),
            ('b', 'c'),
            ('f', 'c'),
            ('f', 'd')
        ]

        self.vertices = sorted(list(set([start for start, end in self.edges] + [end for start, end in self.edges])))
        self.adjacency_matrix_data = self.create_adjacency_matrix(self.vertices, self.edges)
        self.incidence_matrix_data = self.create_incidence_matrix(self.vertices, self.edges)

        self.adjacency_button = ttk.Button(master, text="Показати матрицю суміжності", command=self.show_adjacency_matrix)
        self.adjacency_button.pack(pady=10)

        self.incidence_button = ttk.Button(master, text="Показати матрицю інцидентності", command=self.show_incidence_matrix)
        self.incidence_button.pack(pady=10)

    def create_adjacency_matrix(self, vertices, edges):
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]
        vertex_indices = {vertex: i for i, vertex in enumerate(vertices)}
        for u, v in edges:
            u_index = vertex_indices[u]
            v_index = vertex_indices[v]
            matrix[u_index][v_index] += 1
        return (vertices, vertices, matrix)

    def create_incidence_matrix(self, vertices, edges):
        num_vertices = len(vertices)
        num_edges = len(edges)
        matrix = [[0] * num_edges for _ in range(num_vertices)]
        vertex_indices = {vertex: i for i, vertex in enumerate(vertices)}
        edge_labels = [f"e{i+1}" for i in range(num_edges)]

        for j, (u, v) in enumerate(edges):
            if u == v:  # Петля
                matrix[vertex_indices[u]][j] = 2
            else:
                matrix[vertex_indices[u]][j] = 1
                matrix[vertex_indices[v]][j] = -1
        return (vertices, edge_labels, matrix)

    def show_matrix(self, matrix_data, title):
        if not matrix_data:
            return

        row_headers, col_headers, data = matrix_data
        window = tk.Toplevel(self.master)
        window.title(title)
        text_area = tk.Text(window, height=15, width=40)
        text_area.pack(padx=10, pady=10)

        header_row = "    " + "  ".join(col_headers) + "\n"
        separator = "----" + "--" * len(col_headers) + "\n"
        text_area.insert(tk.END, header_row)
        text_area.insert(tk.END, separator)

        for i, row in enumerate(data):
            row_str = f"{row_headers[i]} | " + "  ".join(map(str, row)) + "\n"
            text_area.insert(tk.END, row_str)

        text_area.config(state=tk.DISABLED)

    def show_adjacency_matrix(self):
        self.show_matrix(self.adjacency_matrix_data, "Матриця Суміжності")

    def show_incidence_matrix(self):
        self.show_matrix(self.incidence_matrix_data, "Матриця Інцідентності")

root = tk.Tk()
app = GraphRepresentationApp(root)
root.mainloop()