#!/usr/bin/env python3
#
# app.py
#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import abspath, dirname, join
import files, layout, gameplay, timer

1234567890123456789012345678901234567890123456789012345678901234567890

"""
Create the App.
"""
class App(tk.Tk):
    # Initialize data.
    _width, _height, _pad = 600,600, 20
    _color = '#663399'
    _number, _numbers = 6, (6,  8,  9,  10,  12,  14,  15,  18,  20,  21,  24,  27,  28,  32,  35,  36,  40,  44,  45,  50,  )
    _imagepath = abspath(join(dirname(__file__), '../cards'))
    _cards = files.card_pathnames(join(_imagepath, 'faces'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        w, h, p = self._width, self._height, self._pad

        self.title('Concentration Game')
        self.configure(background=self._color)
        self.attributes('-topmost',True)
        self.geometry(f"+{p}+{p}")

        # Set default styles.
        frame_style = ttk.Style()
        frame_style.theme_use('default')
        frame_style.configure('TFrame', background=self._color)

        label_style = ttk.Style()
        label_style.theme_use('default')
        label_style.configure('TLabel',
            background=self._color,
            foreground='white',
            font=('Arial', 18))

        # Center frame.
        frm = ttk.Frame(self, width=w, height=h, padding=p)
        frm.grid(row=0, column=0, sticky=None)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create info.
        info = Info(frm)
        info.pack(fill=tk.X, expand=True)
        self._info = info

        # Create game.
        game = Game(frm)
        game.pack(fill=None, expand=True)
        self._game = game

        # Start timer.
        timer.echo = self._info.update_time
        timer.timer.start()

        self.update_and_print()

    def update_and_print(self):
        # Update and print informaton.
        w, h, p = self._width, self._height, self._pad
        self.update()
        print(f"ax={self.winfo_width()}; ay={self.winfo_height()};")
        print(f"ix={self._info.winfo_width()}; iy={self._info.winfo_height()};")
        print(f"gx={self._game.winfo_width()}; gy={self._game.winfo_height()};")
        self.minsize(width=w+p+p, height=h+p+p+self._info.winfo_height())


class Info(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Set up variable.
        self._option = tk.StringVar(self)

        # Create widgets.
        self.create_widgets(self._root()._number, self._root()._numbers)

    def create_widgets(self, number, numbers):
        pad, color = self._root()._pad / 4, self._root()._color

        # Padding for widgets.
        paddings = {'padx': pad, 'pady': pad}

        # Set name style.
        stylen = ttk.Style()
        stylen.theme_use('default')
        stylen.configure('n.TLabel',
            background=color,
            foreground='white',
            font=('Arial', 28))

        # Create name label.
        labeln = ttk.Label(self, text='Concentration Game', style='n.TLabel')
        labeln.grid(row=0, column=0, columnspan=2, sticky='', **paddings)

        # Create prompt label.
        labelp = ttk.Label(self, text='Select the number of card pairs:')
        labelp.grid(row=1, column=0, sticky=tk.W, **paddings)

        # Create option menu including _option variable).
        option_menu = ttk.OptionMenu(
            self,
            self._option,
            number,
            *numbers,
            command=self.option_changed)

        option_menu.grid(row=1, column=1, sticky=tk.E, **paddings)

        # Create score label.
        self.labels = ttk.Label(self, foreground='red')
        self.labels.grid(row=2, column=0, sticky='', **paddings)

        # Create timer label.
        self.labelt = ttk.Label(self, foreground='red', text="00:00")
        self.labelt.grid(row=2, column=1, sticky=tk.E, **paddings)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def option_changed(self, *args):
        timer.reset()
        number = int(self._option.get()) * 2
        # TODO: change this to update score
        self.labels['text'] = f'You selected: {layout.sizing(number)}'
        self._root()._game.create_widgets(number)
        self._root().update_and_print()

    def update_time(self, str):
        self.labelt.configure(text=str)

class Game(ttk.Frame):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        number = self._root()._number

        self.create_widgets(number * 2)

    def on_click(self, button):
        info = button.grid_info()
        row, column = int(info['row']), int(info['column'])
        print(f"({row},{column}) {button.cget('image')} "
              f"back={self._back} card={self._images[row][column]}")

        # Swap face for back or back for face.
        # TODO: integrate this with gameplay
        if str(button.cget('image')[0]) == str(self._back):
            button.configure(image=self._images[row][column])
        else:
            button.configure(image=self._back)

    def clear_frame(self):
       for widgets in self.winfo_children():
          widgets.destroy()

    def create_widgets(self, number):
        gw, gh = self._root()._width, self._root()._height,
        pad, color = self._root()._pad / 2, self._root()._color

        # Clear frame.
        self.clear_frame()

        # Load an image, resize it, create a PhotoImage.
        # https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690
        png = Image.open(join(self._root()._imagepath, 'backs/blue_back.png')).convert('RGB')

        # Calculate the scale.
        nx, ny = layout.sizing(number)
        scale = max((nx * (png.width + pad) + pad) / gw, (ny * (png.height + pad) + pad) / gh)
        w, h = int(png.width / scale - pad), int(png.height / scale - pad)

        print(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {scale:.2f}")
        back = png.resize((w, h,), Image.LANCZOS)
        self._back = ImageTk.PhotoImage(back)

        # Set button style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('game.TButton', background=color, borderwidth=1)

        # Add images and buttons in a grid.
        # TODO: create the real randomized card images.
        # Images references must be remembered.
        cards = self._root()._cards + self._root()._cards
        self._images = [[None for i in range(nx)] for j in range(ny)]
        self._buttons = [[None for i in range(nx)] for j in range(ny)]
        for r in range(ny):
            for c in range(nx):
                # Create scaled PhotoImage.
                png = Image.open(cards[r * nx + c]).convert('RGB')
                face = png.resize((w, h,), Image.LANCZOS)
                self._images[r][c] = ImageTk.PhotoImage(face)
                # Create Button w/ PhotoImage
                self._buttons[r][c] = ttk.Button(self, style='game.TButton', image=self._back)
                self._buttons[r][c].grid(row=r, column=c)
                self._buttons[r][c].configure(command=lambda button=self._buttons[r][c]: self.on_click(button))
        del self._buttons

if __name__ == "__main__":
    app = App()
    app.mainloop()
