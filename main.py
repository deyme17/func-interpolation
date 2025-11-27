from tkinter import Tk
from gui.app_window import InterpolationApp
from methods import interpolation_methods

if __name__ == '__main__':
    root = Tk()
    app = InterpolationApp(
        root, 
        interpolation_methods
    )
    root.mainloop()
