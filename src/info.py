#!/usr/bin/env python3
#
# info.py
#
import tkinter as tk
from tkinter import ttk
import gameplay, layout, log, score

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the Info frame.
"""

logger = log.log(__name__)    # initialize logger

 
class Info(ttk.Frame):
    # Initialize data.
    _after = None

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        number = self._root()._number

        # Reset clock based on number.
        self.reset_clock(number)

        # Set up variable for option menu.
        self._option = tk.StringVar(self)

        # Create widgets.
        self.create_widgets(number, self._root()._numbers)

    def option_changed(self, *args):
        """Game layout has changed, so reset game, clock, and app."""
        gameplay.reset()
        pairs = int(self._option.get())
        logger.info(f"Layout: {layout.sizing(pairs * 2)} for {pairs} pairs")
        self.reset_clock(pairs)
        # Before any score, display the new layout.
        self.update_score(f"You selected: {layout.sizing(pairs * 2)}")
        self._root()._game.create_widgets(pairs)
        self._root().update_and_log()

    def reset_clock(self, pairs, tick=1000):
        """Initialize and start game clock using self.after."""
        if self._after is not None:
            self.after_cancel(self._after)
        self._seconds = score.seconds(pairs) + 1
        self._after = self.after(tick, self.update_clock)

    def update_clock(self, tick=1000):
        """Count down game seconds using self.after and stop at zero."""
        self._seconds -= 1
        mins, secs = int(self._seconds) // 60, int(self._seconds) % 60
        display = f"{mins:02d}:{secs:02d}"
        self._labelc.configure(text=display)
        logger.debug(f"{display} remains")
        if self._seconds > 0:
            self._after = self.after(tick, self.update_clock)

    def update_score(self, str):
        """Callback for updating score label."""
        self._labels.configure(text=str)

    def create_widgets(self, number, numbers):
        pad = self._root()._pad / 4

        # Padding for widgets.
        paddings = {'padx': pad, 'pady': pad}

        # Set name style.
        stylen = ttk.Style()
        stylen.theme_use('default')
        stylen.configure('n.TLabel',
            font=(self._root()._font_family, self._root()._font_size * 2))

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
        self._labels = ttk.Label(self, foreground='red')
        self._labels.grid(row=2, column=0, sticky='', **paddings)

        # Create clock label.
        self._labelc = ttk.Label(self, foreground='red', text="00:00")
        self._labelc.grid(row=2, column=1, sticky=tk.E, **paddings)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Start score.
        score.echo = self.update_score
        score.reset()

if __name__ == "__main__":
    class Test(tk.Tk):
        _pad, _font_family, _font_size = 12, 'Arial', 18
        _number, _numbers = 6, (3,  6,  12,  14,  20,  24,  27,  30,  35,  42,  44,  48,  52, )
        class Object(object): pass
        _game = Object(); _game.create_widgets = lambda x: None

        def __init__(self, **kwargs):
            super().__init__(**kwargs) 
            self.title('Test Info')

            credit = Info(self)
            credit.pack()

        def update_and_log(self):
            pass

    info = Test()
    info.mainloop()
