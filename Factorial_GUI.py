import tkinter as tk
from tkinter import messagebox, ttk

class FactorialVisualizer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.steps = []
        self.current_step = 0
        self.delay = 1000
        self.animation_running = False
        self.call_tree_nodes = {}
        self.return_tree_nodes = {}
        self.call_node_counter = 0
        self.return_node_counter = 0
        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Enter n (0-12):").pack(side=tk.LEFT)
        self.input_entry = tk.Entry(top_frame, width=5)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.run_button = tk.Button(top_frame, text="Run", command=self.prepare_steps)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(top_frame, text="Start", command=self.start_animation, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(top_frame, text="Pause", command=self.pause_animation, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(top_frame, text="Reset", command=self.reset_animation, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.step_button = tk.Button(top_frame, text="Step", command=self.step_forward, state=tk.DISABLED)
        self.step_button.pack(side=tk.LEFT, padx=5)

        tk.Button(top_frame, text="Delay +", command=self.increase_delay).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Delay -", command=self.decrease_delay).pack(side=tk.LEFT, padx=5)

        self.delay_label = tk.Label(top_frame, text=f"Delay: {self.delay / 1000:.1f}s")
        self.delay_label.pack(side=tk.LEFT, padx=10)

        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        stack_frame = tk.Frame(main_frame)
        stack_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        tk.Label(stack_frame, text="Call Stack").pack()
        self.stack_listbox = tk.Listbox(stack_frame, height=20, font=("Consolas", 12))
        self.stack_listbox.pack(fill=tk.BOTH, expand=True)

        heap_frame = tk.Frame(main_frame)
        heap_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        tk.Label(heap_frame, text="Heap (Return Computations)").pack()
        self.heap_listbox = tk.Listbox(heap_frame, height=20, font=("Consolas", 12))
        self.heap_listbox.pack(fill=tk.BOTH, expand=True)

        statement_frame = tk.Frame(main_frame)
        statement_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        tk.Label(statement_frame, text="Statement Under Execution").pack()
        self.statement_label = tk.Label(statement_frame, text="Click 'Run' to start...", font=("Arial", 9), wraplength=250)
        self.statement_label.pack(fill=tk.BOTH, expand=True, pady=5)
        tk.Label(statement_frame, text="Current Expression").pack(pady=(10, 0))
        self.expression_label = tk.Label(statement_frame, text="", font=("Arial", 14), fg="blue")
        self.expression_label.pack(fill=tk.BOTH, expand=True)

        tree_frame = tk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(tree_frame, text="Recursion Tree").pack()
        self.canvas = tk.Canvas(tree_frame, width=1200, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def prepare_steps(self):
        try:
            n = int(self.input_entry.get())
            if n < 0 or n > 12:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter an integer between 0 and 12.")
            return

        # Reset UI and state
        self.stack_listbox.delete(0, tk.END)
        self.heap_listbox.delete(0, tk.END)
        self.statement_label.config(text="Steps generated, click Start or Step.")
        self.expression_label.config(text="")
        self.canvas.delete("all")
        self.steps.clear()
        self.current_step = 0

        self.call_tree_nodes.clear()
        self.return_tree_nodes.clear()
        self.call_node_counter = 0
        self.return_node_counter = 0

        self.simulate_factorial(n, [], None, 600, 40, 300, None)

        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.NORMAL)

    def simulate_factorial(self, n, call_stack, parent_call_node, x, y, offset, parent_return_node=None):
        call_node_id = self.call_node_counter
        self.call_node_counter += 1
        self.call_tree_nodes[call_node_id] = (x, y, f"factorial({n})", parent_call_node)

        call_stack.append(n)
        call_expr = f"Calling factorial({n} - 1) → factorial({n - 1})" if n > 1 else ""
        self.steps.append({
            "action": "push",
            "stack": call_stack.copy(),
            "statement": f"Calling factorial({n})",
            "expression": call_expr if call_expr else f"factorial({n})",
            "node": call_node_id,
            "color": "yellow",
            "type": "call"
        })

        if n == 0 or n == 1:
            return_node_id = self.return_node_counter
            self.return_node_counter += 1
            self.return_tree_nodes[return_node_id] = (x, y + 40, f"factorial({n})", parent_return_node)

            self.steps.append({
                "action": "return",
                "stack": call_stack.copy(),
                "statement": f"Base case reached for factorial({n})",
                "expression": f"return factorial({n}) → 1",
                "node": return_node_id,
                "color": "green",
                "type": "return"
            })
            self.steps.append({"action": "heap", "value": f"factorial({n}) = 1"})
            call_stack.pop()
            return 1, return_node_id

        res_recursive, child_return_node_id = self.simulate_factorial(n - 1, call_stack, call_node_id, x - offset, y + 80, offset / 2, parent_return_node)

        res = n * res_recursive

        return_node_id = self.return_node_counter
        self.return_node_counter += 1
        self.return_tree_nodes[return_node_id] = (x, y + 40, f"factorial({n})", child_return_node_id)

        return_expr = f"return {n} * factorial({n} - 1) → {n} * factorial({n - 1})"
        self.steps.append({
            "action": "return",
            "stack": call_stack.copy(),
            "statement": f"Returning from factorial({n})",
            "expression": return_expr,
            "node": return_node_id,
            "color": "green",
            "type": "return"
        })
        self.steps.append({"action": "heap", "value": f"{n} * factorial({n - 1}) = {res}"})

        call_stack.pop()
        return res, return_node_id

    def start_animation(self):
        self.animation_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.DISABLED)
        self.animate_steps()

    def pause_animation(self):
        self.animation_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.NORMAL)

    def reset_animation(self):
        self.animation_running = False
        self.current_step = 0
        self.stack_listbox.delete(0, tk.END)
        self.heap_listbox.delete(0, tk.END)
        self.statement_label.config(text="Click 'Run' to start...")
        self.expression_label.config(text="")
        self.canvas.delete("all")
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.DISABLED)

    def animate_steps(self):
        if not self.animation_running:
            return
        if self.current_step >= len(self.steps):
            self.statement_label.config(text="Recursion complete.")
            self.expression_label.config(text="")
            return

        self.show_step()
        self.after(self.delay, self.animate_steps)

    def step_forward(self):
        if self.current_step < len(self.steps):
            self.show_step()

    def show_step(self):
        step = self.steps[self.current_step]

        if step["action"] in ("push", "return"):
            self.stack_listbox.delete(0, tk.END)
            for val in reversed(step["stack"]):
                self.stack_listbox.insert(tk.END, f"factorial({val})")
            self.statement_label.config(text=step["statement"])
            self.expression_label.config(text=step["expression"])

            tree_type = step.get("type", "call")
            self.draw_tree(highlight_node=step["node"], color=step["color"], tree_type=tree_type)

        elif step["action"] == "heap":
            self.heap_listbox.insert(tk.END, step["value"])

        self.current_step += 1

    def draw_tree(self, highlight_node, color, tree_type="call"):
        self.canvas.delete("all")
        nodes = self.call_tree_nodes if tree_type == "call" else self.return_tree_nodes

        for node_id, (x, y, _, parent_id) in nodes.items():
            if parent_id is not None and parent_id in nodes:
                px, py, _, _ = nodes[parent_id]
                self.draw_arrow(px, py + 20, x, y - 20)

        for node_id, (x, y, text, _) in nodes.items():
            fill_color = color if node_id == highlight_node else "lightgray"
            outline_color = "black" if node_id == highlight_node else "gray"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=fill_color, outline=outline_color, width=2)
            self.canvas.create_text(x, y, text=text, font=("Arial", 10))

    def draw_arrow(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=2)

    def increase_delay(self):
        self.delay = min(self.delay + 200, 5000)
        self.delay_label.config(text=f"Delay: {self.delay / 1000:.1f}s")

    def decrease_delay(self):
        self.delay = max(self.delay - 200, 100)
        self.delay_label.config(text=f"Delay: {self.delay / 1000:.1f}s")


class MatrixMultiplicationVisualizer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.delay = 1000
        self.animation_running = False
        self.current_step = 0
        self.steps = []

        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Matrix A Rows:").pack(side=tk.LEFT)
        self.a_rows_entry = tk.Entry(top_frame, width=3)
        self.a_rows_entry.pack(side=tk.LEFT, padx=2)
        self.a_rows_entry.insert(0, "2")

        tk.Label(top_frame, text="Cols / Rows:").pack(side=tk.LEFT)
        self.a_cols_entry = tk.Entry(top_frame, width=3)
        self.a_cols_entry.pack(side=tk.LEFT, padx=2)
        self.a_cols_entry.insert(0, "2")

        tk.Label(top_frame, text="Matrix B Cols:").pack(side=tk.LEFT)
        self.b_cols_entry = tk.Entry(top_frame, width=3)
        self.b_cols_entry.pack(side=tk.LEFT, padx=2)
        self.b_cols_entry.insert(0, "2")

        self.run_button = tk.Button(top_frame, text="Run", command=self.prepare_matrices)
        self.run_button.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(top_frame, text="Start", command=self.start_animation, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.pause_button = tk.Button(top_frame, text="Pause", command=self.pause_animation, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.reset_button = tk.Button(top_frame, text="Reset", command=self.reset_animation, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        self.step_button = tk.Button(top_frame, text="Step", command=self.step_forward, state=tk.DISABLED)
        self.step_button.pack(side=tk.LEFT, padx=5)

        tk.Button(top_frame, text="Delay +", command=self.increase_delay).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Delay -", command=self.decrease_delay).pack(side=tk.LEFT, padx=5)

        self.delay_label = tk.Label(top_frame, text=f"Delay: {self.delay / 1000:.1f}s")
        self.delay_label.pack(side=tk.LEFT, padx=10)

        # Canvas for matrices
        self.canvas = tk.Canvas(self, width=1100, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Status text box with scrollbar
        status_frame = tk.Frame(self)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(status_frame, text="Calculation Status").pack()
        self.status_text = tk.Text(status_frame, height=8, font=("Consolas", 11))
        self.status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(status_frame, command=self.status_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.status_text.config(yscrollcommand=scrollbar.set)

    def prepare_matrices(self):
        try:
            a_rows = int(self.a_rows_entry.get())
            a_cols = int(self.a_cols_entry.get())
            b_cols = int(self.b_cols_entry.get())
            if a_rows <= 0 or a_cols <= 0 or b_cols <= 0 or a_cols > 10 or a_rows > 10 or b_cols > 10:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter positive integers ≤ 10.")
            return

        # Generate random small integer matrices or fixed for simplicity
        # Here fixed values for simplicity, but could be randomized or user input
        self.A = [[(i + j + 1) for j in range(a_cols)] for i in range(a_rows)]
        self.B = [[(i * 2 + j + 1) for j in range(b_cols)] for i in range(a_cols)]
        self.C = [[0] * b_cols for _ in range(a_rows)]

        self.a_rows = a_rows
        self.a_cols = a_cols
        self.b_cols = b_cols

        self.steps.clear()
        self.current_step = 0
        self.status_text.delete("1.0", tk.END)
        self.canvas.delete("all")

        self.generate_steps()

        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.NORMAL)

    def generate_steps(self):
        # For each element C[i][j] = sum_k A[i][k]*B[k][j]
        for i in range(self.a_rows):
            for j in range(self.b_cols):
                # Highlight row i in A
                self.steps.append({"action": "highlight_row", "row": i})
                total = 0
                for k in range(self.a_cols):
                    self.steps.append({
                        "action": "highlight_cells",
                        "i": i,
                        "k": k,
                        "k2": k,
                        "j": j,
                        "desc": f"C[{i}][{j}] += A[{i}][{k}] * B[{k}][{j}] = {self.A[i][k]} * {self.B[k][j]} = {self.A[i][k]*self.B[k][j]}"
                    })
                    total += self.A[i][k] * self.B[k][j]
                    self.steps.append({"action": "update_C", "i": i, "j": j, "value": total})
                self.C[i][j] = total
                self.steps.append({"action": "clear_highlight"})

    def start_animation(self):
        self.animation_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.DISABLED)
        self.animate_steps()

    def pause_animation(self):
        self.animation_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.NORMAL)

    def reset_animation(self):
        self.animation_running = False
        self.current_step = 0
        self.status_text.delete("1.0", tk.END)
        self.canvas.delete("all")
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.DISABLED)

    def step_forward(self):
        if self.current_step < len(self.steps):
            self.show_step()

    def animate_steps(self):
        if not self.animation_running:
            return
        if self.current_step >= len(self.steps):
            self.status_text.insert(tk.END, "\nMatrix multiplication complete.\n")
            self.status_text.see(tk.END)
            return
        self.show_step()
        self.after(self.delay, self.animate_steps)

    def show_step(self):
        step = self.steps[self.current_step]

        self.canvas.delete("highlight")
        self.canvas.delete("indices")
        self.canvas.delete("labels")

        self.draw_matrices(highlight_step=step)

        if step["action"] == "highlight_row":
            self.status_text.insert(tk.END, f"\nHighlighting row {step['row']} of A\n")
        elif step["action"] == "highlight_cells":
            desc = step["desc"]
            self.status_text.insert(tk.END, desc + "\n")
        elif step["action"] == "update_C":
            i, j, val = step["i"], step["j"], step["value"]
            self.status_text.insert(tk.END, f"C[{i}][{j}] updated to {val}\n")
        elif step["action"] == "clear_highlight":
            self.status_text.insert(tk.END, "\nClearing highlights\n")

        self.status_text.see(tk.END)

        self.current_step += 1

    def draw_matrices(self, highlight_step):
        cell_w, cell_h = 40, 40
        start_x_a, start_y_a = 50, 50
        start_x_b, start_y_b = 50, 150
        start_x_c, start_y_c = 350, 100

        # Draw Matrix A with indices and highlight row
        for i in range(self.a_rows):
            for j in range(self.a_cols):
                x1 = start_x_a + j * cell_w
                y1 = start_y_a + i * cell_h
                x2 = x1 + cell_w
                y2 = y1 + cell_h
                fill = "white"
                outline = "black"
                if highlight_step["action"] == "highlight_row" and highlight_step["row"] == i:
                    fill = "#ffffcc"
                if highlight_step["action"] == "highlight_cells" and highlight_step["i"] == i and highlight_step["k"] == j:
                    fill = "yellow"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, tags="highlight")
                self.canvas.create_text(x1 + cell_w/2, y1 + cell_h/2, text=str(self.A[i][j]), tags="highlight")
                # indices
                self.canvas.create_text(x1 - 12, y1 + cell_h/2, text=f"A[{i}][{j}]", fill="blue", font=("Arial", 8), tags="indices")

        # Draw Matrix B with indices and highlight cell
        for i in range(self.a_cols):
            for j in range(self.b_cols):
                x1 = start_x_b + j * cell_w
                y1 = start_y_b + i * cell_h
                x2 = x1 + cell_w
                y2 = y1 + cell_h
                fill = "white"
                outline = "black"
                if highlight_step["action"] == "highlight_cells" and highlight_step["k2"] == i and highlight_step["j"] == j:
                    fill = "yellow"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, tags="highlight")
                self.canvas.create_text(x1 + cell_w/2, y1 + cell_h/2, text=str(self.B[i][j]), tags="highlight")
                # indices
                self.canvas.create_text(x1 - 12, y1 + cell_h/2, text=f"B[{i}][{j}]", fill="green", font=("Arial", 8), tags="indices")

        # Draw Matrix C with updated values and highlight cell
        for i in range(self.a_rows):
            for j in range(self.b_cols):
                x1 = start_x_c + j * cell_w
                y1 = start_y_c + i * cell_h
                x2 = x1 + cell_w
                y2 = y1 + cell_h
                fill = "white"
                outline = "black"
                if highlight_step["action"] == "update_C" and highlight_step["i"] == i and highlight_step["j"] == j:
                    fill = "#aaffaa"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, tags="highlight")
                self.canvas.create_text(x1 + cell_w/2, y1 + cell_h/2, text=str(self.C[i][j]), tags="highlight")
                # indices
                self.canvas.create_text(x1 - 12, y1 + cell_h/2, text=f"C[{i}][{j}]", fill="red", font=("Arial", 8), tags="indices")

        # Labels for matrices
        self.canvas.create_text(start_x_a + self.a_cols*cell_w/2, start_y_a - 20, text="Matrix A", font=("Arial", 12, "bold"), tags="labels")
        self.canvas.create_text(start_x_b + self.b_cols*cell_w/2, start_y_b - 20, text="Matrix B", font=("Arial", 12, "bold"), tags="labels")
        self.canvas.create_text(start_x_c + self.b_cols*cell_w/2, start_y_c - 20, text="Matrix C (Result)", font=("Arial", 12, "bold"), tags="labels")

    def increase_delay(self):
        self.delay = min(self.delay + 200, 5000)
        self.delay_label.config(text=f"Delay: {self.delay / 1000:.1f}s")

    def decrease_delay(self):
        self.delay = max(self.delay - 200, 100)
        self.delay_label.config(text=f"Delay: {self.delay / 1000:.1f}s")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Factorial & Matrix Multiplication Visualizer")
        self.geometry("1300x800")

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        self.factorial_tab = FactorialVisualizer(notebook)
        notebook.add(self.factorial_tab, text="Factorial Visualizer")

        self.matrix_tab = MatrixMultiplicationVisualizer(notebook)
        notebook.add(self.matrix_tab, text="Matrix Multiplication Visualizer")


if __name__ == "__main__":
    app = App()
    app.mainloop()
