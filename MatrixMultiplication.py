import tkinter as tk
from tkinter import font

SIZE = 3

matrixA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrixB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultMatrix = [[0] * SIZE for _ in range(SIZE)]


class MatrixMultiplicationAnimation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Multiplication Animation")
        self.geometry("900x600")  # Smaller window size

        self.row = 0
        self.col = 0
        self.k = 0

        self.prev_row = -1
        self.prev_col = -1
        self.prev_k = -1
        self.prev_status_col = -1  # For blank line on col change

        self.delay = 1500  # milliseconds

        self.create_widgets()
        self.after_id = None

    def create_widgets(self):
        # Fonts
        self.font_normal = font.Font(family="Consolas", size=11)

        # Frames for matrices
        self.frameA = tk.Frame(self, padx=5, pady=5)
        self.frameB = tk.Frame(self, padx=5, pady=5)
        self.frameC = tk.Frame(self, padx=5, pady=5)

        self.frameA.grid(row=0, column=0)
        self.frameB.grid(row=1, column=0)
        self.frameC.grid(row=0, column=1, rowspan=2)

        # Titles
        tk.Label(self.frameA, text="Matrix A", font=("Arial", 12)).grid(row=0, column=0, columnspan=SIZE)
        tk.Label(self.frameB, text="Matrix B", font=("Arial", 12)).grid(row=0, column=0, columnspan=SIZE)
        tk.Label(self.frameC, text="Result C", font=("Arial", 12)).grid(row=0, column=0, columnspan=SIZE)

        # Matrix A cells
        self.labelsA = []
        for i in range(SIZE):
            row_labels = []
            for j in range(SIZE):
                frame = tk.Frame(self.frameA, borderwidth=1, relief="solid")
                frame.grid(row=i + 1, column=j, padx=1, pady=1)
                val_label = tk.Label(frame, text=str(matrixA[i][j]), font=self.font_normal, width=3)
                val_label.pack()
                idx_label = tk.Label(frame, text=f"A[{i}][{j}]", font=("Arial", 7))
                idx_label.pack()
                row_labels.append(val_label)
            self.labelsA.append(row_labels)

        # Matrix B cells
        self.labelsB = []
        for i in range(SIZE):
            row_labels = []
            for j in range(SIZE):
                frame = tk.Frame(self.frameB, borderwidth=1, relief="solid")
                frame.grid(row=i + 1, column=j, padx=1, pady=1)
                val_label = tk.Label(frame, text=str(matrixB[i][j]), font=self.font_normal, width=3)
                val_label.pack()
                idx_label = tk.Label(frame, text=f"B[{i}][{j}]", font=("Arial", 7))
                idx_label.pack()
                row_labels.append(val_label)
            self.labelsB.append(row_labels)

        # Result Matrix cells
        self.labelsC = []
        for i in range(SIZE):
            row_labels = []
            for j in range(SIZE):
                frame = tk.Frame(self.frameC, borderwidth=1, relief="solid")
                frame.grid(row=i + 1, column=j, padx=1, pady=1)
                val_label = tk.Label(frame, text="0", font=self.font_normal, width=3)
                val_label.pack()
                idx_label = tk.Label(frame, text=f"C[{i}][{j}]", font=("Arial", 7))
                idx_label.pack()
                row_labels.append(val_label)
            self.labelsC.append(row_labels)

        # Controls
        controls_frame = tk.Frame(self, pady=5)
        controls_frame.grid(row=2, column=0, columnspan=2)

        self.btn_start = tk.Button(controls_frame, text="Start", width=6, command=self.start_animation)
        self.btn_pause = tk.Button(controls_frame, text="Pause", width=6, command=self.pause_animation)
        self.btn_reset = tk.Button(controls_frame, text="Reset", width=6, command=self.reset_animation)

        self.btn_start.grid(row=0, column=0, padx=3)
        self.btn_pause.grid(row=0, column=1, padx=3)
        self.btn_reset.grid(row=0, column=2, padx=3)

        # Delay controls
        delay_frame = tk.Frame(self, pady=5)
        delay_frame.grid(row=3, column=0, columnspan=2)
        tk.Label(delay_frame, text="Delay (ms):", font=("Arial", 10)).grid(row=0, column=0)
        self.lbl_delay = tk.Label(delay_frame, text=str(self.delay), font=("Arial", 10))
        self.lbl_delay.grid(row=0, column=1, padx=5)

        btn_plus = tk.Button(delay_frame, text="+", width=3, command=self.increase_delay)
        btn_minus = tk.Button(delay_frame, text="-", width=3, command=self.decrease_delay)
        btn_plus.grid(row=0, column=2, padx=3)
        btn_minus.grid(row=0, column=3, padx=3)

        # Row/Col/K display
        indices_frame = tk.Frame(self, pady=5)
        indices_frame.grid(row=4, column=0, columnspan=2)

        self.lbl_row = tk.Label(indices_frame, text="row=0", font=("Arial", 10), fg="orange")
        self.lbl_col = tk.Label(indices_frame, text="col=0", font=("Arial", 10), fg="blue")
        self.lbl_k = tk.Label(indices_frame, text="k=0", font=("Arial", 10), fg="red")

        self.lbl_row.grid(row=0, column=0, padx=10)
        self.lbl_col.grid(row=0, column=1, padx=10)
        self.lbl_k.grid(row=0, column=2, padx=10)

        # Status text box with scrollbar
        status_frame = tk.Frame(self)
        status_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.status_text = tk.Text(status_frame, height=24, width=100, font=("Consolas", 9), wrap="none")
        scrollbar = tk.Scrollbar(status_frame, command=self.status_text.yview)
        self.status_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.status_text.config(state=tk.DISABLED)

    def increase_delay(self):
        self.delay += 500
        self.lbl_delay.config(text=str(self.delay))

    def decrease_delay(self):
        if self.delay > 500:
            self.delay -= 500
            self.lbl_delay.config(text=str(self.delay))

    def start_animation(self):
        if self.after_id is None:
            self.animate_step()

    def pause_animation(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

    def reset_animation(self):
        self.pause_animation()
        self.row = 0
        self.col = 0
        self.k = 0
        self.prev_row = -1
        self.prev_col = -1
        self.prev_k = -1
        self.prev_status_col = -1

        for i in range(SIZE):
            for j in range(SIZE):
                resultMatrix[i][j] = 0
                self.labelsC[i][j].config(text="0", fg="black")

        for i in range(SIZE):
            for j in range(SIZE):
                self.labelsA[i][j].config(bg="SystemButtonFace")
                self.labelsB[i][j].config(bg="SystemButtonFace")

        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state=tk.DISABLED)

        self.update_indices(highlight_all=True)
        self.after_id = None

    def update_indices(self, highlight_all=False):
        self.lbl_row.config(text=f"row={self.row}")
        self.lbl_col.config(text=f"col={self.col}")
        self.lbl_k.config(text=f"k={self.k}")

        if highlight_all or self.row != self.prev_row:
            self.flash(self.lbl_row)
        if highlight_all or self.col != self.prev_col:
            self.flash(self.lbl_col)
        if highlight_all or self.k != self.prev_k:
            self.flash(self.lbl_k)

        self.prev_row, self.prev_col, self.prev_k = self.row, self.col, self.k

    def flash(self, lbl):
        original_color = lbl.cget("fg")
        lbl.config(fg="green")
        self.after(200, lambda: lbl.config(fg=original_color))

    def animate_step(self):
        if self.row >= SIZE:
            self.status_text.config(state=tk.NORMAL)
            self.status_text.insert(tk.END, "\nMultiplication complete.\n")
            self.status_text.see(tk.END)
            self.status_text.config(state=tk.DISABLED)
            self.after_id = None
            return

        self.update_indices()

        # Reset highlights
        for i in range(SIZE):
            for j in range(SIZE):
                self.labelsA[i][j].config(bg="SystemButtonFace")
                self.labelsB[i][j].config(bg="SystemButtonFace")
                self.labelsC[i][j].config(bg="SystemButtonFace")

        # Highlight the row in A, current A and B elements, and current C element
        for j in range(SIZE):
            self.labelsA[self.row][j].config(bg="lightyellow")

        self.labelsA[self.row][self.k].config(bg="orange")
        self.labelsB[self.k][self.col].config(bg="lightblue")
        self.labelsC[self.row][self.col].config(bg="lightgreen")

        current_c = resultMatrix[self.row][self.col]
        a = matrixA[self.row][self.k]
        b = matrixB[self.k][self.col]
        product = a * b
        resultMatrix[self.row][self.col] += product
        self.labelsC[self.row][self.col].config(text=str(resultMatrix[self.row][self.col]), fg="blue")

        # Update status with new line when col changes
        self.status_text.config(state=tk.NORMAL)
        if self.col != self.prev_status_col:
            self.status_text.insert(tk.END, "\n")  # New line for new column
            self.prev_status_col = self.col

        line = f"C[{self.row}][{self.col}] = C[{self.row}][{self.col}] + A[{self.row}][{self.k}] * B[{self.k}][{self.col}] --> {current_c} + {a} * {b} = {resultMatrix[self.row][self.col]}\n"
        self.status_text.insert(tk.END, line)
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)

        self.k += 1
        if self.k == SIZE:
            self.k = 0
            self.col += 1
            if self.col == SIZE:
                self.col = 0
                self.row += 1

        self.after_id = self.after(self.delay, self.animate_step)


if __name__ == "__main__":
    app = MatrixMultiplicationAnimation()
    app.mainloop()
