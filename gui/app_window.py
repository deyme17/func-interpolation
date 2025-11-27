from typing import Dict
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

from gui.input_frame import InputFrame
from gui.results_frame import ResultsFrame
from methods.interpolation_method import IInterpolationMethod


class InterpolationApp:
    """Main application controller."""
    def __init__(self, root: tk.Tk, methods: Dict[str, IInterpolationMethod]) -> None:
        self.root = root
        self.root.title("Numeric Methods: Interpolation")
        self.root.geometry("1200x700")
        self._configure_style()

        self.methods = methods
        self.selected_method = tk.StringVar(value=list(methods.keys())[0])

        main_frame = ttk.Frame(root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # left panel
        control_panel = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # method selector
        ttk.Label(control_panel, text="Select Method:").pack(anchor="w", pady=(0, 5))
        method_menu = ttk.OptionMenu(control_panel, self.selected_method, list(methods.keys())[0], *methods.keys())
        method_menu.pack(fill=tk.X, pady=(0, 15))

        # input
        self.input_frame = InputFrame(control_panel)
        self.input_frame.pack(fill=tk.X, pady=(0, 15))

        # calculate btn
        calc_btn = ttk.Button(control_panel, text="CALCULATE", command=self.calculate)
        calc_btn.pack(fill=tk.X, pady=(0, 10))

        # result
        self.results_frame = ResultsFrame(main_frame)
        self.results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def _configure_style(self) -> None:
        """Sets application visual theme."""
        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        style.configure('TLabel', font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'))

    def calculate(self) -> None:
        """Orchestrates the calculation flow."""
        try:
            # 1. Get Data
            data = self.input_frame.get_data()
            x_nodes = data['x_nodes']
            y_nodes = data['y_nodes']
            x_target = data.get('x_target')

            # 2. Get Method
            method_name = self.selected_method.get()
            method = self.methods[method_name]

            # 3. Calculate Specific Target (if provided)
            target_tuple = None
            if x_target is not None:
                y_target = method.interpolate(x_nodes, y_nodes, x_target)
                target_tuple = (x_target, y_target)

            # 4. Generate Smooth Curve for Plotting
            # Create 100 points between min and max X for smooth line
            margin = (max(x_nodes) - min(x_nodes)) * 0.1
            x_smooth = np.linspace(min(x_nodes) - margin, max(x_nodes) + margin, 100)
            y_smooth = np.array([method.interpolate(x_nodes, y_nodes, x) for x in x_smooth])

            # 5. Update UI
            self.results_frame.update_results(x_nodes, y_nodes, x_smooth, y_smooth, target_tuple)

        except Exception as e:
            messagebox.showerror("Computation Error", str(e))