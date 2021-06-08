#!/usr/bin/env python3
#
# main.py
#
from tkinter import *
from PIL import Image, ImageTk
from random import randint
import layout
import threading    # make a new .PY file for threading

"""
Concentration card game. This module currently creates the windows.
"""
1234567890123456789012345678901234567890123456789012345678901234567890
# Create an instance of tkinter frame
win = Tk()

# Dimensions.
ww, wh, pad, grid = 600, 600, 20, (6, 4)

# Set the geometry of tkinter frame.
win.geometry(f"{ww + 2 * pad}x{wh + 2 * pad}+100+100")

# Add a frame, centered in the window.
# https://stackoverflow.com/questions/4241036/how-do-i-center-a-frame-within-a-frame-in-tkinter
frm = Frame(win, bd=10, bg='#663399', width=ww, height=wh)
frm.grid(row=0, column=0, sticky='')
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
        
# Load an image, resize it, create a PhotoImage.
# https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690
png = Image.open("./cards/green_back.png").convert('RGB')

# Calculate the scale.
nx, ny = grid
scale = max((nx * (png.width + pad) + pad) / ww, (ny * (png.height + pad) + pad) / wh)
w, h = int(png.width / scale - pad), int(png.height / scale - pad)

print(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {scale:.2f}")
png = png.resize((w, h,), Image.LANCZOS)
img = ImageTk.PhotoImage(png)

# Define button callback.
def on_click(button):
    info = button.grid_info()
    position = (int(info['row']), int(info['column'], ), )
    print(f"{position} {button.cget('image')}")

# Add buttons in a grid.
nx, ny = grid
buttons = ny * [ nx * [None]]
for r in range(ny):
    for c in range(nx):
        # TODO: not sure why 4 works
        buttons[r][c] = Button(frm, bd=pad / 4, image=img)
        buttons[r][c].grid(row=r, column=c)
        buttons[r][c].configure(command=lambda button=buttons[r][c]: on_click(button))

# Update and print informaton.
win.update()
print(f"x={frm.winfo_width()}; y={frm.winfo_height()};")

win.mainloop()
