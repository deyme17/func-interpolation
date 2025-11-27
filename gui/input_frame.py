from typing import Dict, Any
from tkinter import ttk
import numpy as np


class InputFrame(ttk.Frame):
    """Frame for input data"""
    def __init__(self, parent):
        super().__init__(parent)
        self.entries = {}
        self._create_widgets()

    def _create_widgets(self) -> None:
        pass

    def get_data(self) -> Dict[str, Any]:
        """Parses and returns data from inputs"""
        data = {}
        try:
            pass
        except Exception as e:
            raise ValueError(f"Input parsing error: {e}")
        return data