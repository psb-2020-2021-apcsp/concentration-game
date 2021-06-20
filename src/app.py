#!/usr/bin/env python3
#
# app.py
#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random, sys
from os.path import abspath, dirname, join
import files, layout, gameplay, log, timer

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the App.
"""

logger = log.log(__name__)    # initialize logger


class App(tk.Tk):
    # Initialize data.
    _width, _height, _pad = 600,600, 20
    _color = '#663399'
    _number, _numbers = 6, (3,  6,  12,  14,  20,  24,  27,  30,  35,  42,  44,  48,  52, )
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
        timer.fsm = gameplay.fsm
        self._timer = timer.run_timer()
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

        # Start gameplay.
        gameplay.show_face = self._game.show_face
        gameplay.show_back = self._game.show_back
        gameplay.get_id = self._game.get_id
        gameplay.echo = self._info.update_score
        gameplay.reset()

        self.update_and_log()

    def update_and_log(self):
        # Update and log informaton.
        w, h, p = self._width, self._height, self._pad
        self.update()
        logger.info(f"wx={self.winfo_width()}; wy={self.winfo_height()};")
        logger.info(f"ix={self._info.winfo_width()}; iy={self._info.winfo_height()};")
        logger.info(f"gx={self._game.winfo_width()}; gy={self._game.winfo_height()};")

        # Set minimum app size.
        self.minsize(width=w+p+p, height=h+p+p+self._info.winfo_height())

    def on_closing(self):
        """Stop timer, destroy app, and exit."""
        timer.done = True
        self._timer.join()
        self.destroy()
        sys.exit()


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
        gameplay.reset()
        pairs = int(self._option.get())
        # TODO: change this to update score
        self.update_score(f"You selected: {layout.sizing(pairs * 2)}")
        self._root()._game.create_widgets(pairs)
        self._root().update_and_log()

    def update_score(self, str):
        self.labels.configure(text=str)

    def update_time(self, str):
        self.labelt.configure(text=str)


class Game(ttk.Frame):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        number = self._root()._number

        self.create_widgets(number)

    def _show_image(self, image, row, col):
        """Show image on button at (row, column, )."""
        button = self._buttons[row][col]
        button.configure(image=image)

    def show_face(self, signal):
        """Show the card face on button at (row, column, )."""
        row, col = signal
        self._show_image(self._images[row][col], row, col)

    def show_back(self, signal):
        """Show the card back on button at (row, column, )."""
        row, col = signal
        self._show_image(self._back, row, col)

    def get_id(self, signal):
        """Get id for image at (row, column, )."""
        row, col = signal
        return str(self._images[row][col])

    def on_click(self, button):
        info = button.grid_info()
        row, col = int(info['row']), int(info['column'])
        logger.info(f"click: ({row},{col}) "
            f"back={self._back} card={self._images[row][col]} "
            f"{button.cget('image')} ")
        gameplay.fsm((row, col, ))

    def clear_frame(self):
       for widgets in self.winfo_children():
          widgets.destroy()

    def create_widgets(self, pairs):
        gw, gh = self._root()._width, self._root()._height,
        pad, color = self._root()._pad / 2, self._root()._color

        # Clear frame.
        self.clear_frame()

        # Load an image, resize it, create a PhotoImage.
        # https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690
        png = Image.open(join(self._root()._imagepath, 'backs/blue_back.png')).convert('RGB')

        # Calculate the scale.
        nx, ny = layout.sizing(pairs * 2)
        scale = max((nx * (png.width + pad) + pad) / gw, (ny * (png.height + pad) + pad) / gh)
        w, h = int(png.width / scale - pad), int(png.height / scale - pad)

        logger.info(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {scale:.2f}")
        back = png.resize((w, h,), Image.LANCZOS)
        self._back = ImageTk.PhotoImage(back)

        # Set button style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('game.TButton', background=color, borderwidth=1)


        # TODO: put this in files?
        # Create list of random paths for each pair of cards.
        paths = random.sample(self._root()._cards, len(self._root()._cards))[: pairs]
        # Create list of PhotoImages from list of random paths.
        cards = [ ImageTk.PhotoImage(Image
            .open(path)
            .convert('RGB')
            .resize((w, h,), Image.LANCZOS)) for path in paths ]
        # Create random list of image pairs.
        images = random.sample(cards + cards, pairs * 2)

        # Add images and buttons in a grid.
        # PhotoImages references must be remembered.
        self._images = [[None for i in range(nx)] for j in range(ny)]
        self._buttons = [[None for i in range(nx)] for j in range(ny)]
        for r in range(ny):
            for c in range(nx):
                # Add image to _images grid.
                self._images[r][c] = images[r * nx + c]
                # Create configured Button and add to _buttons grid.
                self._buttons[r][c] = ttk.Button(self, style='game.TButton', image=self._back)
                self._buttons[r][c].grid(row=r, column=c)
                self._buttons[r][c].configure(command=lambda button=self._buttons[r][c]: self.on_click(button))

if __name__ == "__main__":
    app = App()
    app.mainloop()
