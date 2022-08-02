import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.root = tk.Tk()
        self.root.title(title)

        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = width, height

        self.root.geometry(f"{w}x{h}+{int(sw/2-w/2)}+{int(sh/2-h/2)}")

    def set_label(self) -> None:
        label = ttk.Label(self.root, text="Test")
        label.pack()

    def _update(self) -> None:
        self.root.update_idletasks()

    def _run(self) -> None:
        self.root.mainloop()

    def _close(self) -> None:
        self.root.destroy()
