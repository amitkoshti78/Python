import tkinter as tk
from tkinter import messagebox
import time
import threading

NODE_RADIUS = 20
LEVEL_HEIGHT = 80

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0
        self.color = "white"


class SearchStep:
    def __init__(self, current_node, call_stack, visited_nodes, next_node=None):
        self.current_node = current_node
        self.call_stack = call_stack[:]
        self.visited_nodes = visited_nodes[:]
        self.next_node = next_node


class BSTVisualizer:
    def __init__(self, root):
        self.root_window = root
        self.root_window.title("BST Recursive Search Visualizer")

        self.tree_root = None
        self.previous_tree = None
        self.search_steps = []
        self.current_step_index = 0
        self.running = False
        self.paused = False

        # --- Top Frame (Controls) ---
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack(side=tk.TOP)

        tk.Label(top_frame, text="Insert:").pack(side=tk.LEFT)
        self.insert_entry = tk.Entry(top_frame, width=10)
        self.insert_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Insert", command=self.insert_value).pack(side=tk.LEFT, padx=5)

        tk.Label(top_frame, text="Search:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(top_frame, width=10)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Search", command=self.start_search).pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(top_frame, text="Clear Graph", command=self.clear_graph)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        self.undo_btn = tk.Button(top_frame, text="Undo", command=self.undo_clear, state="disabled")
        self.undo_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(top_frame, text="Delete Node", command=self.delete_node)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # --- Canvas for Tree ---
        self.canvas = tk.Canvas(root, width=800, height=500, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # --- Right Frame (Stacks) ---
        right_frame = tk.Frame(root, padx=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(right_frame, text="Recursive Call Stack", font=("Arial", 12, "bold")).pack()
        self.stack_box = tk.Listbox(right_frame, width=30, height=15)
        self.stack_box.pack(pady=5)

        tk.Label(right_frame, text="Visited Nodes", font=("Arial", 12, "bold")).pack()
        self.visited_box = tk.Listbox(right_frame, width=30, height=10)
        self.visited_box.pack(pady=5)

    # ---------------- Core Tree Functions ----------------
    def insert_value(self):
        try:
            val = int(self.insert_entry.get().strip())
            self.tree_root = self.insert_node(self.tree_root, val)
            self.insert_entry.delete(0, tk.END)
            self.redraw_tree()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter an integer value.")

    def insert_node(self, node, val):
        if node is None:
            return BSTNode(val)
        if val < node.val:
            node.left = self.insert_node(node.left, val)
        elif val > node.val:
            node.right = self.insert_node(node.right, val)
        return node

    def redraw_tree(self):
        self.canvas.delete("all")
        if self.tree_root is None:
            return
        self.compute_positions(self.tree_root, 0, 400)
        self.draw_edges(self.tree_root)
        self.draw_nodes(self.tree_root)

    def compute_positions(self, node, depth, x):
        if node is None:
            return
        node.y = 50 + depth * LEVEL_HEIGHT
        if node.left:
            self.compute_positions(node.left, depth + 1, x - 80)
        node.x = x
        if node.right:
            self.compute_positions(node.right, depth + 1, x + 80)

    def draw_edges(self, node):
        if node is None:
            return
        if node.left:
            self.canvas.create_line(node.x, node.y, node.left.x, node.left.y)
            self.draw_edges(node.left)
        if node.right:
            self.canvas.create_line(node.x, node.y, node.right.x, node.right.y)
            self.draw_edges(node.right)

    def draw_nodes(self, node):
        if node is None:
            return
        self.canvas.create_oval(node.x - NODE_RADIUS, node.y - NODE_RADIUS,
                                node.x + NODE_RADIUS, node.y + NODE_RADIUS,
                                fill=node.color, outline="black")
        self.canvas.create_text(node.x, node.y, text=str(node.val), font=("Arial", 12))
        self.draw_nodes(node.left)
        self.draw_nodes(node.right)

    def reset_colors(self, node):
        if node is None:
            return
        node.color = "white"
        self.reset_colors(node.left)
        self.reset_colors(node.right)

    # ---------------- Search Visualization ----------------
    def start_search(self):
        if not self.tree_root:
            messagebox.showwarning("Empty Tree", "Please insert values first.")
            return
        try:
            target = int(self.search_entry.get().strip())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter an integer value.")
            return

        self.reset_colors(self.tree_root)
        self.stack_box.delete(0, tk.END)
        self.visited_box.delete(0, tk.END)
        self.search_steps = []
        self.current_step_index = 0

        self.generate_search_steps(self.tree_root, target, [], [])

        if not self.search_steps:
            messagebox.showwarning("Search Error", "No steps generated.")
            return

        if not self.running:
            self.running = True
            threading.Thread(target=self.play_steps).start()

    def generate_search_steps(self, node, target, call_stack, visited_nodes):
        call_stack.append(f"search({node.val if node else 'null'}, {target})")

        if node is None:
            self.search_steps.append(SearchStep(None, call_stack, visited_nodes))
            call_stack.pop()
            return False

        visited_nodes.append(node.val)
        self.search_steps.append(SearchStep(node, call_stack, visited_nodes))

        if node.val == target:
            self.search_steps.append(SearchStep(node, call_stack, visited_nodes))
            call_stack.pop()
            return True
        elif target < node.val:
            self.search_steps.append(SearchStep(node, call_stack, visited_nodes, node.left))
            found = self.generate_search_steps(node.left, target, call_stack, visited_nodes)
            call_stack.pop()
            return found
        else:
            self.search_steps.append(SearchStep(node, call_stack, visited_nodes, node.right))
            found = self.generate_search_steps(node.right, target, call_stack, visited_nodes)
            call_stack.pop()
            return found

    def play_steps(self):
        for step in self.search_steps:
            self.reset_colors(self.tree_root)
            if step.current_node:
                step.current_node.color = "yellow"
            if step.next_node:
                step.next_node.color = "lightblue"
            self.redraw_tree()

            self.stack_box.delete(0, tk.END)
            for i, call in enumerate(step.call_stack):
                self.stack_box.insert(tk.END, call)
                if i == len(step.call_stack) - 1:
                    self.stack_box.itemconfig(i, bg="yellow")

            self.visited_box.delete(0, tk.END)
            for v in step.visited_nodes:
                self.visited_box.insert(tk.END, v)

            time.sleep(1)
        self.running = False

    # ---------------- New Features ----------------
    def clear_graph(self):
        if self.tree_root is None:
            return

        self.previous_tree = self.clone_tree(self.tree_root)
        self.tree_root = None
        self.search_steps = []
        self.canvas.delete("all")
        self.canvas.create_text(400, 250, text="Graph Cleared", font=("Arial", 20), fill="gray")

        self.stack_box.delete(0, tk.END)
        self.visited_box.delete(0, tk.END)

        self.insert_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

        self.undo_btn.config(state="normal")

    def undo_clear(self):
        if self.previous_tree:
            self.tree_root = self.previous_tree
            self.redraw_tree()
            self.undo_btn.config(state="disabled")

    def clone_tree(self, node):
        if node is None:
            return None
        new_node = BSTNode(node.val)
        new_node.color = node.color
        new_node.left = self.clone_tree(node.left)
        new_node.right = self.clone_tree(node.right)
        return new_node

    def delete_node(self):
        try:
            val = int(self.insert_entry.get().strip())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Enter a valid integer to delete.")
            return

        self.animate_delete(val)

    def animate_delete(self, val):
        node = self.find_node(self.tree_root, val)
        if node:
            for _ in range(3):  # Flash effect
                node.color = "red"
                self.redraw_tree()
                time.sleep(0.3)
                node.color = "white"
                self.redraw_tree()
                time.sleep(0.3)

            self.tree_root = self._delete(self.tree_root, val)
            self.redraw_tree()
        else:
            messagebox.showinfo("Delete Node", f"Node {val} not found.")
        self.insert_entry.delete(0, tk.END)

    def find_node(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        elif val < node.val:
            return self.find_node(node.left, val)
        else:
            return self.find_node(node.right, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._min_value(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    root.mainloop()
