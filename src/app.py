#!/usr/bin/env python3
#
# app.py
#
import tkinter as tk
from tkinter import ttk
import sys
from os.path import abspath, dirname, join
import info, game, credit
import files, log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the App.
"""

logger = log.log(__name__)    # initialize logger


class App(tk.Tk):
    # Initialize data.
    _width, _height, _pad = 500, 500, 12
    _color = '#663399'
    _font_family, _font_size = 'Arial', 18
    _number, _numbers = 6, (3,  6,  12,  14,  20,  24,  27,  30,  35,  42,  44,  48,  52, )
    _imagepath = abspath(join(dirname(__file__), '../cards'))
    _cards = files.card_pathnames(join(_imagepath, 'faces'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 

        self.title('Concentration Game')
        self.configure(background=self._color)
        self.attributes('-topmost',True)
        self.geometry(f"+{self._pad}+{self._pad}")
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
            font=(self._font_family, self._font_size, ))

        button_style = ttk.Style()
        button_style.theme_use('default')
        button_style.configure('TButton', background=self._color, borderwidth=0)

        self.create_widgets()

    def on_closing(self):
        """Destroy app and exit."""
        logger.info(f"Window closing...")
        self.destroy()
        sys.exit()

    def update_and_log(self):
        """Update tk app and log information."""
        w, h, p = self._width, self._height, self._pad
        self.update()

        # To make sure app-size minima are correct, use reqwidth & reqheight!
        logger.info(f"wx={self.winfo_reqwidth()}; wy={self.winfo_reqheight()};")
        logger.info(f"ix={self._info.winfo_reqwidth()}; iy={self._info.winfo_reqheight()};")
        logger.info(f"gx={self._game.winfo_reqwidth()}; gy={self._game.winfo_reqheight()};")
        logger.info(f"cx={self._credit.winfo_reqwidth()}; cy={self._credit.winfo_reqheight()};")

        mx = max(self._info.winfo_reqwidth(), self._game.winfo_reqwidth(), self._credit.winfo_reqwidth())
        my = self._game.winfo_reqheight()
        logger.info(f"mx={mx}; my={my};")
        ih, ch = self._info.winfo_reqheight(), self._credit.winfo_reqheight()
        logger.info(f" x={mx+p+p};  y={my+p+p+ih+ch};")

        # Set minimum app size.
        self.minsize(width=mx+p+p,height=my+p+p+ih+ch)

        # TODO: use these font-size and winfo logs
        log_string_dimension('HELLO WORLD!')
        log_winfo(self)

    def create_widgets(self):
        w, h, p = self._width, self._height, self._pad

        # Center frame.
        frm = ttk.Frame(self, width=w, height=h, padding=p)
        frm.grid(row=0, column=0, sticky=None)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create info.
        infow = info.Info(frm)
        infow.pack(fill=tk.X, expand=True)
        self._info = infow

        # Create game.
        gamew = game.Game(frm)
        gamew.pack(fill=None, expand=True)
        self._game = gamew

        # Create credit.
        creditw = credit.Credit(frm)
        creditw.pack(fill=tk.X, expand=True)
        self._credit = creditw

        self.update_and_log()

def log_string_dimension(string, name='Arial', size=14, log=logger.debug):
    """Log width, height of string in font name / size."""
    from tkinter.font import Font
    tkfont = Font(family=name, size=size)
    log(f"(width, height) of '{string}': {(tkfont.measure(string), tkfont.metrics('linespace'))}")

def log_winfo(widget, log=logger.debug):
    """Log all winfo properties of widget."""
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html
    atom = widget.winfo_atom(widget)
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
