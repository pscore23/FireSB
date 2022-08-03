import tkinter as tk
from tkinter import filedialog, ttk


class MainWindow(tk.Frame):
    def __init__(self, width: int, height: int, title: str) -> None:
        self.root = tk.Tk()
        super().__init__(self.root)

        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = width, height

        self.root.title(title)
        self.root.geometry(f"{w}x{h}+{int(sw/2-w/2)}+{int(sh/2-h/2)}")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def run(self) -> None:
        self._update()
        self.root.mainloop()

    def _update(self) -> None:
        self.root.update_idletasks()

    def _close(self) -> None:
        self.root.destroy()

    def set_label(self, text: str) -> None:
        label = ttk.Label(self.frame, text=text)
        label.pack()
