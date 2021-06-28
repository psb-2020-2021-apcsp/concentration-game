#!/usr/bin/env python3
#
# game.py
#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import join
import random
import gameplay, layout, log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Create the Game.
"""

logger = log.log(__name__)    # initialize logger


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
        """When button clicked, advance gameplay based on clicked card."""
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
        """Cancel self._after."""
        self.after_cancel(self._after)

    def clear_frame(self):
        """Destroy all card buttons in anticipation of creating a new game."""
        for widgets in self.winfo_children():
            widgets.destroy()

    def create_widgets(self, pairs):
        gw, gh = self._root()._width, self._root()._height
        pad = self._root()._pad // 2

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

        # Create card back PhotoImage.
        logger.info(f"Card from: {png.width}x{png.height} to: {w}x{h} is a scale of {divisor:.2f}")
        back = png.resize((w, h,), Image.LANCZOS)
        self._back = ImageTk.PhotoImage(back)
        logger.info(f"Image dimensions: {self._back.width()}x{self._back.height()}")

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
                self._buttons[r][c] = ttk.Button(self, image=self._back)
                self._buttons[r][c].grid(row=r, column=c)
                self._buttons[r][c].configure(
                    command=lambda button=self._buttons[r][c]: self.on_click(button))

        # Start gameplay.
        gameplay.show_face = self.show_face
        gameplay.show_back = self.show_back
        gameplay.get_id = self.get_id
        gameplay.start_delay = self.start_delay
        gameplay.stop_delay = self.stop_delay
        gameplay.reset()

if __name__ == "__main__":
    from os.path import abspath, dirname, join
    import files
    class Test(tk.Tk):
        _number, _width, _height, _pad, = 6, 500, 500, 12
        _imagepath = abspath(join(dirname(__file__), '../cards'))
        _cards = files.card_pathnames(join(_imagepath, 'faces'))

        def __init__(self, **kwargs):
            super().__init__(**kwargs) 
            self.title('Test Game')

            game = Game(self)
            game.pack()

    game = Test()
    game.mainloop()
