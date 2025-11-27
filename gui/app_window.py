from typing import Dict
import tkinter as tk
from tkinter import ttk, messagebox
from gui.input_frame import InputFrame
from gui.results_frame import ResultsFrame
from methods import IInterpolationMethod


class InterpolationApp:
    """Main application class"""
    def __init__(self, root: tk.Tk, methods: Dict[str, IInterpolationMethod]) -> None:
        self.root = root
        self.root.title("Function Interpolation")
        self.root.geometry("900x650")
        self._configure_style()

        self.methods = methods

        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        # input section
        # Calculate Button
        # result section

    def _configure_style(self) -> None:
        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        style.configure('TLabel', font=('Segoe UI', 9))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'))

    def calculate(self) -> None:
        try:
            pass
        except Exception as e:
            messagebox.showerror("Computation Error", str(e))