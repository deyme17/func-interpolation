import tkinter as tk
from typing import Dict, Any
from tkinter import ttk
import numpy as np


class InputFrame(ttk.Frame):
    """Frame for data input (Nodes and Target)."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        self.entries: Dict[str, ttk.Entry] = {}
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Initializes input fields and labels."""
        self.columnconfigure(1, weight=1)

        # x
        ttk.Label(self, text="X Nodes (space separated):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entries['x_nodes'] = ttk.Entry(self)
        self.entries['x_nodes'].grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # y
        ttk.Label(self, text="Y Nodes (space separated):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entries['y_nodes'] = ttk.Entry(self)
        self.entries['y_nodes'].grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # target x
        ttk.Label(self, text="Target X (to evaluate):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entries['x_target'] = ttk.Entry(self)
        self.entries['x_target'].grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    def get_data(self) -> Dict[str, Any]:
        """Parses and validates user input strings into arrays."""
        data = {}
        try:
            # x
            x_str = self.entries['x_nodes'].get().replace(',', ' ')
            data['x_nodes'] = np.array([float(x) for x in x_str.split()], dtype=float)

            # y
            y_str = self.entries['y_nodes'].get().replace(',', ' ')
            data['y_nodes'] = np.array([float(y) for y in y_str.split()], dtype=float)
            
            # target x
            target_str = self.entries['x_target'].get()
            data['x_target'] = float(target_str) if target_str else None

            # validation
            if len(data['x_nodes']) != len(data['y_nodes']):
                raise ValueError("X and Y arrays must have the same length.")
            if len(data['x_nodes']) < 2:
                raise ValueError("At least 2 points are required.")
            if len(data['x_nodes']) != len(set(data['x_nodes'])):
                raise ValueError("X nodes must be unique.")
        except ValueError as e:
            raise ValueError(f"Input Error: {e}")
        return data