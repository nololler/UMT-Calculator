import tkinter as tk
from ttkbootstrap import Style


class RightMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")  # Adjust as needed

        self.style = Style("darkly")

        # Create a top bar with Machines button
        self.topbar = tk.Frame(root, bg="#222")
        self.topbar.pack(side="top", fill="x")

        self.machines_btn = tk.Button(
            self.topbar, text="Machines", command=self.toggle_menu)
        self.machines_btn.pack(side="right", padx=10, pady=5)

        # Right slide-out menu (initially hidden)
        self.menu_frame = tk.Frame(
            root, bg="#333", width=200, height=self.root.winfo_height())
        self.menu_visible = False
        self.menu_frame.place(x=self.root.winfo_width(), y=0)

        # Add placeholder square buttons
        for i in range(5):
            btn = tk.Button(self.menu_frame,
                            text=f"Button {i+1}", width=10, height=3)
            btn.pack(pady=10)

        # Update the menu height with the root
        self.root.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.menu_frame.config(height=event.height)
        if self.menu_visible:
            self.menu_frame.place(
                x=event.width - self.menu_frame.winfo_width(), y=0)
        else:
            self.menu_frame.place(x=event.width, y=0)

    def toggle_menu(self):
        width = self.menu_frame.winfo_width()
        if not self.menu_visible:
            self.menu_frame.place(x=self.root.winfo_width() - width, y=0)
        else:
            self.menu_frame.place(x=self.root.winfo_width(), y=0)
        self.menu_visible = not self.menu_visible


if __name__ == "__main__":
    root = tk.Tk()
    app = RightMenuApp(root)
    root.mainloop()
