#!/usr/bin/env python3
#
# app.py
#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random, sys, webbrowser
from os.path import abspath, dirname, join
import files, layout, gameplay, log, score

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the App.
"""

logger = log.log(__name__)    # initialize logger


class App(tk.Tk):
    # Initialize data.
    _width, _height, _pad = 500, 500, 12
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
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

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

        # Create credit.
        credit = Credit(frm)
        credit.pack(fill=tk.X, expand=True)
        self._credit = credit

        # Start gameplay.
        gameplay.show_face = self._game.show_face
        gameplay.show_back = self._game.show_back
        gameplay.get_id = self._game.get_id
        gameplay.start = self._game.start_delay
        gameplay.stop = self._game.stop_delay
        gameplay.reset()

        # Start score.
        score.echo = self._info.update_score
        score.reset()

        self.update_and_log()

    def update_and_log(self):
        # Update and log informaton.
        w, h, p = self._width, self._height, self._pad
        self.update()

        # To make sure app-size minima are correct, use reqwidth & reqheight!
        logger.info(f"wx={self.winfo_reqwidth()}; wy={self.winfo_reqheight()};")
        logger.info(f"ix={self._info.winfo_reqwidth()}; iy={self._info.winfo_reqheight()};")
        logger.info(f"gx={self._game.winfo_reqwidth()}; gy={self._game.winfo_reqheight()};")
        logger.info(f"cx={self._credit.winfo_reqwidth()}; cy={self._credit.winfo_reqheight()};")

        # Set minimum app size.
        mx = max(self._info.winfo_reqwidth(), self._game.winfo_reqwidth(), self._credit.winfo_reqwidth())
        my = self._game.winfo_reqheight()
        logger.info(f"mx={mx}; my={my};")
        ih, ch = self._info.winfo_reqheight(), self._credit.winfo_reqheight()
        logger.info(f" x={mx+p+p};  y={my+p+p+ih+ch};")
        self.minsize(width=mx+p+p,height=my+p+p+ih+ch)

        # TODO: use these font-size and winfo logs
        self.log_string_dimension('HELLO WORLD!')
        self.log_winfo(self)

    def on_closing(self):
        """Stop timer, destroy app, and exit."""
        logger.info(f"Window closing...")
        self.destroy()
        sys.exit()

    def log_string_dimension(self, string, name='Arial', size=14, log=logger.debug):
        """Log width, height of string in font name / size."""
        from tkinter.font import Font
        tkfont = Font(family=name, size=size)
        log(f"(width, height) of '{string}': {(tkfont.measure(string), tkfont.metrics('linespace'))}")

    def log_winfo(self, widget, log=logger.debug):
        """Log all winfo properties of widget."""
        # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html
        atom = widget.winfo_atom(self)
        log(f"winfo_atom = {atom}")
        log(f"winfo_atomname = {widget.winfo_atomname(atom)}")
        log(f"winfo_cells = {widget.winfo_cells()}")
        log(f"winfo_children = {widget.winfo_children()}")
        log(f"winfo_class = {widget.winfo_class()}")
        log(f"winfo_colormapfull = {widget.winfo_colormapfull()}")
        pointerx, pointery = widget.winfo_pointerx(), widget.winfo_pointery()
        log(f"winfo_containing = {widget.winfo_containing(pointerx, pointery)}")
        log(f"winfo_depth = {widget.winfo_depth()}")
        log(f"winfo_exists = {widget.winfo_exists()}")
        log(f"winfo_fpixels = {widget.winfo_fpixels('1i')}")
        log(f"winfo_geometry = {widget.winfo_geometry()}")
        log(f"winfo_height = {widget.winfo_height()}")
        id = widget.winfo_id()
        log(f"winfo_id = {id}")
        log(f"winfo_interps = {widget.winfo_interps()}")
        log(f"winfo_ismapped = {widget.winfo_ismapped()}")
        log(f"winfo_manager = {widget.winfo_manager()}")
        log(f"winfo_name = {widget.winfo_name()}")
        log(f"winfo_parent = {widget.winfo_parent()}")
        log(f"winfo_pathname = {widget.winfo_pathname(id)}")
        log(f"winfo_pixels = {widget.winfo_pixels('1i')}")
        log(f"winfo_pointerx = {pointerx}")
        log(f"winfo_pointerxy = {widget.winfo_pointerxy()}")
        log(f"winfo_pointery = {pointery}")
        log(f"winfo_reqheight = {widget.winfo_reqheight()}")
        log(f"winfo_reqwidth = {widget.winfo_reqwidth()}")
        log(f"winfo_rgb = {widget.winfo_rgb('#639')}")
        log(f"winfo_rootx = {widget.winfo_rootx()}")
        log(f"winfo_rooty = {widget.winfo_rooty()}")
        log(f"winfo_screen = {widget.winfo_screen()}")
        log(f"winfo_screencells = {widget.winfo_screencells()}")
        log(f"winfo_screendepth = {widget.winfo_screendepth()}")
        log(f"winfo_screenheight = {widget.winfo_screenheight()}")
        log(f"winfo_screenmmheight = {widget.winfo_screenmmheight()}")
        log(f"winfo_screenmmwidth = {widget.winfo_screenmmwidth()}")
        log(f"winfo_screenvisual = {widget.winfo_screenvisual()}")
        log(f"winfo_screenwidth = {widget.winfo_screenwidth()}")
        log(f"winfo_server = {widget.winfo_server()}")
        log(f"winfo_toplevel = {widget.winfo_toplevel()}")
        log(f"winfo_viewable = {widget.winfo_viewable()}")
        log(f"winfo_visual = {widget.winfo_visual()}")
        log(f"winfo_visualid = {widget.winfo_visualid()}")
        log(f"winfo_visualsavailable = {widget.winfo_visualsavailable()}")
        log(f"winfo_vrootheight = {widget.winfo_vrootheight()}")
        log(f"winfo_vrootwidth = {widget.winfo_vrootwidth()}")
        log(f"winfo_vrootx = {widget.winfo_vrootx()}")
        log(f"winfo_vrooty = {widget.winfo_vrooty()}")
        log(f"winfo_width = {widget.winfo_width()}")
        log(f"winfo_x = {widget.winfo_x()}")
        log(f"winf_y = {widget.winfo_y()}")


class Info(ttk.Frame):
    # Initialize data.
    _after = None

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        number = self._root()._number

        # Reset clock based on number.
        self.reset_clock(number)

        # Set up variable.
        self._option = tk.StringVar(self)

        # Create widgets.
        self.create_widgets(number, self._root()._numbers)

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

        # Create clock label.
        self.labelc = ttk.Label(self, foreground='red', text="00:00")
        self.labelc.grid(row=2, column=1, sticky=tk.E, **paddings)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def option_changed(self, *args):
        gameplay.reset()
        pairs = int(self._option.get())
        logger.info(f"Layout: {layout.sizing(pairs * 2)} for {pairs} pairs")
        self.reset_clock(pairs)
        # Before any score, display the new layout.
        self.update_score(f"You selected: {layout.sizing(pairs * 2)}")
        self._root()._game.create_widgets(pairs)
        self._root().update_and_log()

    def update_score(self, str):
        self.labels.configure(text=str)

    def reset_clock(self, pairs, tick=1000):
        if self._after is not None:
            self.after_cancel(self._after)
        self._seconds = score.seconds(pairs) + 1
        self._after = self.after(tick, self.update_clock)

    def update_clock(self, tick=1000):
        self._seconds -= 1
        mins, secs = int(self._seconds) // 60, int(self._seconds) % 60
        display = f"{mins:02d}:{secs:02d}"
        self.labelc.configure(text=display)
        logger.debug(f"{display} remains")
        if self._seconds > 0:
            self._after = self.after(tick, self.update_clock)


class Game(ttk.Frame):
    # Initialize data.
    _after = None
    
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

    def start_delay(self, delay=2000):
        """When timed out, invoke gameplay.fsm()."""
        self._after = self.after(delay, gameplay.fsm)

    def stop_delay(self):
        """Cancel self.after."""
        self.after_cancel(self._after)

    def clear_frame(self):
       for widgets in self.winfo_children():
          widgets.destroy()

    def create_widgets(self, pairs):
        gw, gh = self._root()._width, self._root()._height,
        pad, color = self._root()._pad // 2, self._root()._color

        # Clear frame.
        self.clear_frame()

        # Load an image, resize it, create a PhotoImage.
        # https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690
        png = Image.open(join(self._root()._imagepath, 'backs/blue_back.png')).convert('RGB')

        # Calculate the scale.
        nx, ny = layout.sizing(pairs * 2)
        scale = lambda n, d, wh: (n * (d + pad) + pad) / wh
        divisor = max(scale(nx, png.width, gw), scale(ny, png.height, gh))
        w, h = int(png.width / divisor - pad), int(png.height / divisor - pad)

        logger.info(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {divisor:.2f}")
        back = png.resize((w, h,), Image.LANCZOS)
        self._back = ImageTk.PhotoImage(back)
        logger.info(f"Image dimensions: {self._back.width()}x{self._back.height()}")

        # Set button style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('game.TButton', background=color, borderwidth=0)

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

class Credit(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create widgets.
        self.create_widgets()

    def on_click(self, event):
        webbrowser.open_new(event.widget.cget("text"))

    def create_widgets(self):
        pad, color = self._root()._pad / 4, self._root()._color

        # Padding for widgets.
        paddings_nw = {'padx': (0, pad // 2, ), 'pady': (pad, pad // 2, )}
        paddings_ne = {'padx': (pad // 2, 0, ), 'pady': (pad, pad // 2, )}
        paddings_sw = {'padx': (0, pad // 2, ), 'pady': (pad // 2, pad, )}
        paddings_se = {'padx': (pad // 2, 0, ), 'pady': (pad // 2, pad, )}

        # Set credit style.
        stylec = ttk.Style()
        stylec.theme_use('default')
        stylec.configure('c.TLabel',
            background=color,
            foreground='white',
            font=('Arial', 14, ))

        # Set link style.
        stylel = ttk.Style()
        stylel.theme_use('default')
        stylel.configure('l.TLabel',
            background=color,
            foreground='white',
            font=('Arial', 14, 'underline', ))

        # Create repo credit label.
        labelrc = ttk.Label(self, text='Repository:', style='c.TLabel')
        labelrc.grid(row=0, column=0, sticky=tk.E, **paddings_nw)

        # Create repo link label.
        rl = r'https://github.com/psb-2020-2021-apcsp/concentration-game'
        labelrl = ttk.Label(self, text=rl, cursor='right_ptr', style='l.TLabel')
        labelrl.bind('<Button-1>', self.on_click)
        labelrl.grid(row=0, column=1, sticky=tk.W, **paddings_ne)

        # Create image credit label.
        labelic = ttk.Label(self, text='Image Credit:', style='c.TLabel')
        labelic.grid(row=1, column=0, sticky=tk.E, **paddings_sw)

        # Create image link label.
        il = r'http://acbl.mybigcommerce.com/52-playing-cards/'
        labelil = ttk.Label(self, text=il, cursor='right_ptr', style='l.TLabel')
        labelil.bind('<Button-1>', self.on_click)
        labelil.grid(row=1, column=1, sticky=tk.W, **paddings_se)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
