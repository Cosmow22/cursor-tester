import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys, os

from cursor_frame import CursorFrame

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # chemin temporaire PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = tk.Tk()
gif_path = resource_path("assets/pulse.gif")
gif = Image.open(gif_path)
frames = []

try:
    while True:
        frame = gif.copy()
        frames.append(ImageTk.PhotoImage(frame))
        gif.seek(len(frames))
except EOFError:
    pass

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - 250)
y_cordinate = int((screen_height/2) - 270)

window.geometry(f"500x500+{x_cordinate}+{y_cordinate}")
window.title("Cursor Tester")
icon_path = resource_path("assets/arrow.ico")
window.iconbitmap(icon_path)
window.resizable(False, False)
window.columnconfigure((0, 1, 2), weight=1)
window.rowconfigure((0, 1, 3), weight=1)

CursorFrame(window, (0,0), "arrow", "Normal Select", frames)
CursorFrame(window, (0,1), "watch", "Working in Background", frames)
CursorFrame(window, (0,2), "question_arrow", "Help Select", frames)
CursorFrame(window, (1,0), "no", "Unavailable", frames)
CursorFrame(window, (1,1), "xterm", "Text Select", frames)
CursorFrame(window, (1,2), "sb_v_double_arrow", "Vertical Resize", frames)
CursorFrame(window, (2,0), "sb_h_double_arrow", "Horizontal Resize", frames)
CursorFrame(window, (2,1), "size_nw_se", "Diagonal Resize", frames)
CursorFrame(window, (2,2), "fleur", "Move", frames)

btn = ttk.Button(window, text="Open mouse settings", command=lambda: subprocess.run("main.cpl", shell=True))
btn.grid(row=3, columnspan=3)

window.mainloop()