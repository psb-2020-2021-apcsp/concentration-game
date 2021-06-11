#!/usr/bin/env python3
#
# test.py
#
# https://www.pythontutorial.net/tkinter/tkinter-optionmenu/
#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import layout

1234567890123456789012345678901234567890123456789012345678901234567890

_ww, _wh, _pad = 600, 600, 20
numbers = (6,  8,  9,  10,  12,  14,  15,  18,  20,  21,  24,  27,  28,  32,  35,  36,  40,  44,  45,  50,  )
number = 12
color = '#663399'

"""
Create the App.
"""
class App(tk.Tk):
    # Initialize data.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #self.geometry(f"{self._ww + 2 * self._pad}x{self._wh + 2 * self._pad}"
        #    f"+{2 * self._pad}+{2 * self._pad}")
        self.title('Concentration Game')
        self.configure(background=color)

        # Set style.
        frame_style = ttk.Style()
        frame_style.theme_use('default')
        frame_style.configure('TFrame', background=color)
        label_style = ttk.Style()
        label_style.theme_use('default')
        label_style.configure('TLabel',
            background=color,
            foreground='white',
            font=('Arial', 18))

        # Center frame.
        frm = ttk.Frame(self, width=600, height=600, padding=20)
        frm.grid(row=0, column=0, sticky='')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create info.
        info = Info(frm)
        info.pack(fill=tk.X)
        self._info = info

        # Create game.
        game = Game(frm)
        game.pack(fill=tk.X)
        self._game = game

        self.update_and_print()

    def update_and_print(self):
        # Update and print informaton.
        self.update()
        print(f"ax={self.winfo_width()}; ay={self.winfo_height()};")
        print(f"ix={self._info.winfo_width()}; iy={self._info.winfo_height()};")
        print(f"gx={self._game.winfo_width()}; gy={self._game.winfo_height()};")
        self.minsize(width=600+20+20, height=600+20+20+self._info.winfo_height())

class Info(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # set up variable
        self._option = tk.StringVar(self)

        # create widgets
        self.create_widgets(number, numbers)

    def create_widgets(self, number, numbers):
        """
        # Get frame attributes.
        fw, fh, pad = (int(tcl_obj.string)
            for tcl_obj in (self['width'], self['height'], self['padding'][0], ))
        print(fw, fh, pad)
        """
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # name label
        labeln = ttk.Label(self, text='Concentration Game')
        labeln.grid(row=0, column=0, columnspan=2, sticky='', **paddings)

        # prompt label
        labelp = ttk.Label(self, text='Select the number of card pairs:')
        labelp.grid(row=1, column=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self._option,
            number,
            *numbers,
            command=self.option_changed)

        option_menu.grid(row=1, column=1, sticky=tk.E, **paddings)

        # score label
        self.labels = ttk.Label(self, foreground='red')
        self.labels.grid(row=2, column=0, sticky='', **paddings)

        # timer label
        self.labelt = ttk.Label(self, foreground='green', text="01:00")
        self.labelt.grid(row=2, column=1, sticky=tk.E, **paddings)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def option_changed(self, *args):
        number = int(self._option.get()) * 2
        self.labels['text'] = f'You selected: {layout.sizing(number)}'
        self.master.master._game.create_widgets(number)
        self.master.master.update_and_print()

class Game(ttk.Frame):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.create_widgets(number)

    def on_click(self, button):
        info = button.grid_info()
        position = (int(info['row']), int(info['column'], ), )
        print(f"{position} {button.cget('image')}")

    def clear_frame(self):
       for widgets in self.winfo_children():
          widgets.destroy()

    def create_widgets(self, number):
        """
        # Get frame attributes.
        fw, fh, pad = (int(tcl_obj.string)
            for tcl_obj in (self['width'], self['height'], self['padding'][0], ))
        """
        # Clear frame.
        self.clear_frame()

        # Load an image, resize it, create a PhotoImage.
        # https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690
        png = Image.open("./cards/blue_back.png").convert('RGB')

        # Calculate the scale.
        gw, gh, pad = 600, 600, 10
        nx, ny = layout.sizing(number)
        scale = max((nx * (png.width + pad) + pad) / gw, (ny * (png.height + pad) + pad) / gh)
        w, h = int(png.width / scale - pad), int(png.height / scale - pad)

        print(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {scale:.2f}")
        png = png.resize((w, h,), Image.LANCZOS)
        self._img = ImageTk.PhotoImage(png)

        # Set button style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('game.TButton', background=color, borderwidth=1)

        # Add buttons in a grid.
        self._buttons = ny * [ nx * [None]]
        for r in range(ny):
            for c in range(nx):
                # TODO: not sure why 4 works
                self._buttons[r][c] = ttk.Button(self, style='game.TButton', image=self._img)
                self._buttons[r][c].grid(row=r, column=c)
                self._buttons[r][c].configure(command=lambda button=self._buttons[r][c]: self.on_click(button))

if __name__ == "__main__":
    app = App()
    app.mainloop()
