import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser, font as tkFont

class NotepadPlusPlus:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad++")
        self.root.geometry("800x600")

        # Create a Notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Create a menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # File Menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Tab", command=self.new_tab, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Undo", command=self.undo_text, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.redo_text, accelerator="Ctrl+Y")

        # Format Menu
        self.format_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Bold", command=self.toggle_bold, accelerator="Ctrl+B")
        self.format_menu.add_command(label="Italic", command=self.toggle_italic, accelerator="Ctrl+I")
        self.format_menu.add_command(label="Underline", command=self.toggle_underline, accelerator="Ctrl+U")
        self.format_menu.add_command(label="Font Color", command=self.change_font_color, accelerator="Ctrl+Shift+C")
        self.format_menu.add_command(label="Select Font", command=self.select_font)

        # Bind shortcuts to actions
        self.bind_shortcuts()

        # Create the first tab
        self.new_tab()

    def bind_shortcuts(self):
        """Bind keyboard shortcuts to functions."""
        self.root.bind('<Control-n>', lambda event: self.new_tab())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-q>', lambda event: self.root.quit())
        
        # Edit shortcuts
        self.root.bind('<Control-x>', lambda event: self.cut_text())
        self.root.bind('<Control-c>', lambda event: self.copy_text())
        self.root.bind('<Control-v>', lambda event: self.paste_text())
        self.root.bind('<Control-z>', lambda event: self.undo_text())
        self.root.bind('<Control-y>', lambda event: self.redo_text())

        # Format shortcuts
        self.root.bind('<Control-b>', lambda event: self.toggle_bold())
        self.root.bind('<Control-i>', lambda event: self.toggle_italic())
        self.root.bind('<Control-u>', lambda event: self.toggle_underline())
        
    def new_tab(self):
        """Create a new tab with a text area."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Untitled")
        
        text_area = tk.Text(tab, wrap='word', undo=True)  # Enable undo/redo
        
        # Configure the text area to support tags for formatting
        text_area.tag_configure("bold", font=("Arial", 12, "bold"))
        text_area.tag_configure("italic", font=("Arial", 12, "italic"))
        text_area.tag_configure("underline", font=("Arial", 12, "underline"))
        
        text_area.pack(expand=True, fill='both')
        
        # Add the text area to the tab's frame for later access
        tab.text_area = text_area
        
    def open_file(self):
        """Open a file for editing in a new tab."""
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
        
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                # Create a new tab for the opened file
                tab = ttk.Frame(self.notebook)
                tab_title = file_path.split('/')[-1]  # Use filename as tab title
                self.notebook.add(tab, text=tab_title)  
                
                text_area = tk.Text(tab, wrap='word', undo=True)  # Enable undo/redo
                
                # Configure the text area to support tags for formatting
                text_area.tag_configure("bold", font=("Arial", 12, "bold"))
                text_area.tag_configure("italic", font=("Arial", 12, "italic"))
                text_area.tag_configure("underline", font=("Arial", 12, "underline"))
                
                text_area.pack(expand=True, fill='both')
                text_area.insert(tk.END, content)  # Insert the content into the text area
                
                # Add the text area to the tab's frame for later access
                tab.text_area = text_area
                
                # Switch to the newly opened tab
                self.notebook.select(tab)

    def save_file(self):
         """Save the current content of the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area

         file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt"),
                                                               ("All Files", "*.*")])
         
         if file_path:
             with open(file_path, 'w') as file:
                 content = current_text_area.get(1.0, tk.END)  # Get all content
                 file.write(content)  # Write to the file

    def cut_text(self):
         """Cut selected text from the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
         current_text_area.event_generate("<<Cut>>")

    def copy_text(self):
         """Copy selected text from the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
         current_text_area.event_generate("<<Copy>>")

    def paste_text(self):
         """Paste text into the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
         current_text_area.event_generate("<<Paste>>")

    def undo_text(self):
         """Undo last action in the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
         current_text_area.edit_undo()

    def redo_text(self):
         """Redo last undone action in the active tab."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
         current_text_area.edit_redo()

    def toggle_bold(self):
         """Toggle bold formatting on selected text."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
        
         if current_text_area.tag_ranges("bold"):
             current_text_area.tag_remove("bold", "sel.first", "sel.last")
             return
        
         current_text_area.tag_add("bold", "sel.first", "sel.last")

    def toggle_italic(self):
         """Toggle italic formatting on selected text."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
        
         if current_text_area.tag_ranges("italic"):
             current_text_area.tag_remove("italic", "sel.first", "sel.last")
             return
        
         current_text_area.tag_add("italic", "sel.first", "sel.last")

    def toggle_underline(self):
         """Toggle underline formatting on selected text."""
         current_tab = self.notebook.select()
         current_text_area = self.notebook.nametowidget(current_tab).text_area
        
         if current_text_area.tag_ranges("underline"):
             current_text_area.tag_remove("underline", "sel.first", "sel.last")
             return
        
         current_text_area.tag_add("underline", "sel.first", "sel.last")

    def change_font_color(self):
         """Change font color of selected text."""
         color_code = colorchooser.askcolor(title ="Choose Text Color")[1]
         if color_code:
             current_tab = self.notebook.select()
             current_text_area = self.notebook.nametowidget(current_tab).text_area
             start_index = "sel.first"
             end_index = "sel.last"
             if start_index and end_index:
                 current_text_area.tag_add("color_tag", start_index, end_index)
                 current_text_area.tag_configure("color_tag", foreground=color_code)

    def select_font(self):
         """Open a dialog to select font and size."""
         font_selection_window = tk.Toplevel(self.root)
         font_selection_window.title("Select Font")

         tk.Label(font_selection_window, text="Font Family:").grid(row=0, column=0)
         
         font_family_var = tk.StringVar(value="Arial")
         
         font_family_entry = ttk.Combobox(font_selection_window,
                                           textvariable=font_family_var,
                                           values=tkFont.families())
         
         font_family_entry.grid(row=0, column=1)

         tk.Label(font_selection_window, text="Font Size:").grid(row=1, column=0)
         
         font_size_var = tk.IntVar(value=12)

         font_size_entry = ttk.Combobox(font_selection_window,
                                         textvariable=font_size_var,
                                         values=list(range(8, 73)))
         
         font_size_entry.grid(row=1, column=1)

         apply_button = ttk.Button(font_selection_window,
                                   text="Apply",
                                   command=lambda: 
                                   (self.apply_font(font_family_var.get(), font_size_var.get()),
                                    font_selection_window.destroy()))
         
         apply_button.grid(row=2, columnspan=2)

    def apply_font(self, family, size):
          """Apply selected font family and size to selected text."""
          if not family or not size:
              return

          current_tab = self.notebook.select()
          current_text_area = self.notebook.nametowidget(current_tab).text_area

          start_index = "sel.first"
          end_index = "sel.last"
          
          if start_index and end_index:
              tag_name = f"font_{family}_{size}"
              
              # Remove any existing tags with this name
              if current_text_area.tag_exists(tag_name):
                  current_text_area.tag_remove(tag_name, start_index, end_index)

              # Create a new tag with selected font properties
              current_text_area.tag_configure(tag_name, font=(family, size))
              
              # Apply new tag to selected range
              current_text_area.tag_add(tag_name, start_index, end_index)

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = NotepadPlusPlus(root)
    root.mainloop()

if __name__ == "__main__":
    main()
