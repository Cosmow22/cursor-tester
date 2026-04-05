import tkinter as tk
from tkinter import ttk


class CursorFrame(tk.Frame):
    def __init__(
            self, 
            parent:tk.Tk, 
            position:tuple, 
            cursor:str, 
            name:str,
            frames:list, 
            add_padding=False):
        super().__init__(parent)# )#width=120, height=120
        self.parent = parent
        self.row, self.col = position
        self.cursor = cursor
        self.frames = frames
        #self.grid_propagate(False)
        self.border = tk.Frame(self, background="black", borderwidth=2)
        #self.border.pack(expand=True, fill="both")
        self.animation = ttk.Label(self.border, padding=20)
        self.animation.configure(image=self.frames[0])
        self.label = ttk.Label(self, text=f"{name}")
        self.grid_columnconfigure(0, weight=1)  # permet au label de s’étirer sans déborder
        self.is_hovered = False
        self.i_frame = 0
        self.bind("<Enter>", self.hover)
        self.bind("<Leave>", self.leave)
        self.animation.pack(expand=True, fill="both")
        self.border.grid(row=0, column=0)
        self.label.grid(row=1, column=0, sticky="s")
        self.grid(row=self.row, column=self.col, pady=20, padx=20)
        
    def update_animation(self):
        self.i_frame += 1
        if self.i_frame == 60: self.i_frame = 0
        self.animation.configure(image=self.frames[self.i_frame])
        if self.is_hovered: self.parent.after(30, self.update_animation)

    def hover(self, event):
        self.is_hovered = True
        self.after(0, self.update_animation)
        self.config(cursor=self.cursor)

    def leave(self, event): 
        self.is_hovered = False
        self.i_frame = 0
