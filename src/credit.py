#!/usr/bin/env python3
#
# app.py
#
import tkinter as tk
from tkinter import ttk
import webbrowser
import log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the App.
"""

logger = log.log(__name__)    # initialize logger


class Credit(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create widgets.
        self.create_widgets()

    def on_click(self, event):
        """When label clicked, open a webbrowser to the text URI."""
        webbrowser.open_new(event.widget.cget("text"))

    def create_widgets(self):
        pad = self._root()._pad / 4
        family, size = self._root()._font_family, int(self._root()._font_size * 3 / 4)

        # Padding for widgets.
        paddings_nw = {'padx': (0, pad // 2, ), 'pady': (pad, pad // 2, )}
        paddings_ne = {'padx': (pad // 2, 0, ), 'pady': (pad, pad // 2, )}
        paddings_sw = {'padx': (0, pad // 2, ), 'pady': (pad // 2, pad, )}
        paddings_se = {'padx': (pad // 2, 0, ), 'pady': (pad // 2, pad, )}

        # Set credit style.
        stylec = ttk.Style()
        stylec.theme_use('default')
        stylec.configure('c.TLabel', font=(family, size, ))

        # Set link style.
        stylel = ttk.Style()
        stylel.theme_use('default')
        stylel.configure('l.TLabel', font=(family, size, 'underline', ))

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
    class Test(tk.Tk):
        _pad, _font_family, _font_size = 12, 'Arial', 18

        def __init__(self, **kwargs):
            super().__init__(**kwargs) 
            self.title('Test Credit')

            credit = Credit(self)
            credit.pack()

    credit = Test()
    credit.mainloop()
