import os
import tkinter as tk
from tkinter import filedialog, ttk


class MainWindow(tk.Frame):
    def __init__(self, width: int, height: int, title: str) -> None:
        self.root = tk.Tk()
        super().__init__(self.root)

        self.label, self.button, self.file_name, self.flag = None, None, "", 0

        self.file_name_var = tk.StringVar()
        self.file_name_var.set("解析したい .sb3 ファイルの絶対パス:\r\n未選択")

        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = width, height

        self.root.title(title)
        self.root.geometry(f"{w}x{h}+{int(sw/2-w/2)}+{int(sh/2-h/2)}")

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=1, fill=tk.BOTH)

        self.set_button("エクスプローラーを参照...", 10, 50, self.open_file)
        self.set_button("解析する!", 30, 70, self.main_call)

        self.set_label(150, 40, self.file_name_var)

        self.run()

    def run(self) -> None:
        self._update()
        self.root.mainloop()

    def _update(self) -> None:
        self.root.update_idletasks()

    def close(self) -> None:
        self.root.destroy()

    def open_file(self, event) -> None:
        f_type = [("Scratch プロジェクトファイル", "*.sb3")]
        i_dir = os.path.abspath(os.path.dirname(__file__))
        self.file_name = filedialog.askopenfilename(filetypes=f_type, initialdir=i_dir)

        if not len(self.file_name) == 0:
            self.file_name_var.set(f"解析したい .sb3 ファイルの絶対パス:\r\n{self.file_name}")

    def set_label(self, pos_x: float, pos_y: float, text_var) -> None:
        self.label = ttk.Label(self.frame, textvariable=text_var)
        self.label.place(x=pos_x, y=pos_y)

    def set_button(self, text: str, pos_x: float, pos_y: float, handler) -> None:
        self.button = ttk.Button(self.frame, text=text)
        self.button.bind("<ButtonPress>", handler)
        self.button.place(x=pos_x, y=pos_y)

    def main_call(self, event) -> None:
        self.flag = 1
