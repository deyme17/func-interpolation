import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ResultsFrame(ttk.Frame):
    """Frame for plotting and text results."""
    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self.figure = None
        self.ax = None
        self.canvas = None
        self.result_label = None
        self._init_ui()

    def _init_ui(self) -> None:
        """Sets up plot canvas and result text area."""
        # text
        self.result_label = ttk.Label(self, text="Result: N/A", font=('Segoe UI', 11, 'bold'))
        self.result_label.pack(pady=(0, 10))

        # plot
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self._config_axis()

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _config_axis(self) -> None:
        """Resets axis labels and grid."""
        self.ax.set_title("Interpolation Function")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True, linestyle='--', alpha=0.6)

    def update_results(self, x_nodes: np.ndarray, y_nodes: np.ndarray, 
                       x_smooth: np.ndarray, y_smooth: np.ndarray, 
                       target_res: tuple[float, float] = None) -> None:
        """Updates the plot and result text."""
        self.ax.clear()
        
        # interpolation curve
        self.ax.plot(x_smooth, y_smooth, 'b-', label='Interpolated Polynomial')

        # nodes
        self.ax.plot(x_nodes, y_nodes, 'ro', label='Given Nodes', markersize=6)

        # target points
        if target_res:
            tx, ty = target_res
            self.ax.plot(tx, ty, 'g*', markersize=12, label='Target Point')
            self.result_label.config(text=f"Result: y({tx}) ≈ {ty:.5f}")
        else:
            self.result_label.config(text="Result: Plot updated")

        self._config_axis()
        self.ax.legend()
        self.canvas.draw()