import numpy as np
from .interpolation_method import IInterpolationMethod

class NewtonInterpolation(IInterpolationMethod):
    """Implements Newton Polynomial using Divided Differences."""
    def interpolate(self, x_nodes: np.ndarray, y_nodes: np.ndarray, x_target: float) -> float:
        """Computes value using Newton form."""
        coeffs = self._divided_diff(x_nodes, y_nodes)
        n = len(x_nodes) - 1
        p = coeffs[n]

        for k in range(1, n + 1):
            p = coeffs[n - k] + (x_target - x_nodes[n - k]) * p

        return p
    
    def _divided_diff(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Computes the divided difference table coefficients."""
        n = len(y)
        coeff = np.zeros([n, n])
        coeff[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                coeff[i][j] = (coeff[i + 1][j - 1] - coeff[i][j - 1]) / (x[i + j] - x[i])

        return coeff[0, :]

    def get_name(self) -> str:
        """Returns method name."""
        return "Newton"