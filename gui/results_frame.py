import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ResultsFrame(ttk.Frame):
    """Frame for displaying result solution and function"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.figure = None
        self.ax = None
        self.canvas = None
        self._init_plot()

    def _init_plot(self) -> None:
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("BVP Solution y(x)")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_plot(self, x: np.ndarray, y: np.ndarray) -> None:
        self.ax.clear()
        self.ax.plot(x, y, 'b.-', label='Numerical Solution')
        self.ax.set_title("BVP Solution y(x)")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()