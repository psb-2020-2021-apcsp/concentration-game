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
__all__ = ["App", ]
__author__ = "https://github.com/psb-2020-2021-apcsp/"
__copyright__ = "Copyright 2021, Public Schools of Brookline 2020-2021 APCS-P"
__license__ = "https://choosealicense.com/licenses/mit/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Development"

logger = log.log(__name__)  # initialize logger


class App(tk.Tk):
    # Initialize data.
    _width, _height, _pad = 600, 600, 20
    _color = '#663399'
    _font_family, _font_size = 'Arial', 18
    _number, _numbers = 6, (3,  6,  12,  14,  20,  24,  27,
                            30,  35,  42,  44, 48,  52, )
    _path = abspath(join(dirname(__file__), '../cards'))
    _cards = files.card_pathnames(join(_path, 'faces'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 

        self.title('Concentration Game')
        self.configure(background=self._color)
        self.attributes('-topmost', True)
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

        # Create widgets.
        self._info, self._game, self._credit = self.create_widgets()

        self.update_and_log()

    def on_closing(self):
        """Destroy app and exit."""
        logger.info(f"Window closing...")
        self.destroy()
        sys.exit()

    def update_and_log(self):
        """Update tk app, set minimum app size, and log information."""
        w, h, p = self._width, self._height, self._pad
        self.update()

        # To make sure app-size minima are correct, use reqwidth & reqheight!
        logger.info(f"wx={self.winfo_reqwidth()}; "
                    f"wy={self.winfo_reqheight()};")
        logger.info(f"ix={self._info.winfo_reqwidth()}; "
                    f"iy={self._info.winfo_reqheight()};")
        logger.info(f"gx={self._game.winfo_reqwidth()}; "
                    f"gy={self._game.winfo_reqheight()};")
        logger.info(f"cx={self._credit.winfo_reqwidth()}; "
                    f"cy={self._credit.winfo_reqheight()};")

        mx = max(self._info.winfo_reqwidth(),
                 self._game.winfo_reqwidth(),
                 self._credit.winfo_reqwidth())
        my = self._game.winfo_reqheight()
        logger.info(f"mx={mx}; my={my};")
        ih, ch = self._info.winfo_reqheight(), self._credit.winfo_reqheight()
        logger.info(f" x={mx+p+p};  y={my+p+p+ih+ch};")

        # Set minimum app size.
        self.minsize(width=mx+p+p, height=my+p+p+ih+ch)

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
        inw = info.Info(frm)
        inw.pack(fill=tk.X, expand=True)

        # Create game.
        gmw = game.Game(frm)
        gmw.pack(fill=None, expand=True)

        # Create credit.
        crw = credit.Credit(frm)
        crw.pack(fill=tk.X, expand=True)

        return inw, gmw, crw


def log_string_dimension(string, name='Arial', size=14, logw=logger.debug):
    """Log width, height of string in font name / size."""
    from tkinter.font import Font
    tkfont = Font(family=name, size=size)
    logw(f"(width, height) of '{string}': "
        f"{(tkfont.measure(string), tkfont.metrics('linespace'))}")


def log_winfo(widget, logw=logger.debug):
    """Log all winfo properties of widget."""
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html
    atom = widget.winfo_atom(widget)
    logw(f"winfo_atom = {atom}")
    logw(f"winfo_atomname = {widget.winfo_atomname(atom)}")
    logw(f"winfo_cells = {widget.winfo_cells()}")
    logw(f"winfo_children = {widget.winfo_children()}")
    logw(f"winfo_class = {widget.winfo_class()}")
    logw(f"winfo_colormapfull = {widget.winfo_colormapfull()}")
    pointerx, pointery = widget.winfo_pointerx(), widget.winfo_pointery()
    logw(f"winfo_containing = {widget.winfo_containing(pointerx, pointery)}")
    logw(f"winfo_depth = {widget.winfo_depth()}")
    logw(f"winfo_exists = {widget.winfo_exists()}")
    logw(f"winfo_fpixels = {widget.winfo_fpixels('1i')}")
    logw(f"winfo_geometry = {widget.winfo_geometry()}")
    logw(f"winfo_height = {widget.winfo_height()}")
    wid = widget.winfo_id()
    logw(f"winfo_id = {wid}")
    logw(f"winfo_interps = {widget.winfo_interps()}")
    logw(f"winfo_ismapped = {widget.winfo_ismapped()}")
    logw(f"winfo_manager = {widget.winfo_manager()}")
    logw(f"winfo_name = {widget.winfo_name()}")
    logw(f"winfo_parent = {widget.winfo_parent()}")
    logw(f"winfo_pathname = {widget.winfo_pathname(wid)}")
    logw(f"winfo_pixels = {widget.winfo_pixels('1i')}")
    logw(f"winfo_pointerx = {pointerx}")
    logw(f"winfo_pointerxy = {widget.winfo_pointerxy()}")
    logw(f"winfo_pointery = {pointery}")
    logw(f"winfo_reqheight = {widget.winfo_reqheight()}")
    logw(f"winfo_reqwidth = {widget.winfo_reqwidth()}")
    logw(f"winfo_rgb = {widget.winfo_rgb('#639')}")
    logw(f"winfo_rootx = {widget.winfo_rootx()}")
    logw(f"winfo_rooty = {widget.winfo_rooty()}")
    logw(f"winfo_screen = {widget.winfo_screen()}")
    logw(f"winfo_screencells = {widget.winfo_screencells()}")
    logw(f"winfo_screendepth = {widget.winfo_screendepth()}")
    logw(f"winfo_screenheight = {widget.winfo_screenheight()}")
    logw(f"winfo_screenmmheight = {widget.winfo_screenmmheight()}")
    logw(f"winfo_screenmmwidth = {widget.winfo_screenmmwidth()}")
    logw(f"winfo_screenvisual = {widget.winfo_screenvisual()}")
    logw(f"winfo_screenwidth = {widget.winfo_screenwidth()}")
    logw(f"winfo_server = {widget.winfo_server()}")
    logw(f"winfo_toplevel = {widget.winfo_toplevel()}")
    logw(f"winfo_viewable = {widget.winfo_viewable()}")
    logw(f"winfo_visual = {widget.winfo_visual()}")
    logw(f"winfo_visualid = {widget.winfo_visualid()}")
    logw(f"winfo_visualsavailable = {widget.winfo_visualsavailable()}")
    logw(f"winfo_vrootheight = {widget.winfo_vrootheight()}")
    logw(f"winfo_vrootwidth = {widget.winfo_vrootwidth()}")
    logw(f"winfo_vrootx = {widget.winfo_vrootx()}")
    logw(f"winfo_vrooty = {widget.winfo_vrooty()}")
    logw(f"winfo_width = {widget.winfo_width()}")
    logw(f"winfo_x = {widget.winfo_x()}")
    logw(f"winf_y = {widget.winfo_y()}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
