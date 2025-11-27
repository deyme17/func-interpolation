import numpy as np
from .interpolation_method import IInterpolationMethod

class LagrangeInterpolation(IInterpolationMethod):
    """Implements Lagrange Polynomial Interpolation."""
    def interpolate(self, x_nodes: np.ndarray, y_nodes: np.ndarray, x_target: float) -> float:
        """Computes value using Lagrange basis polynomials."""
        n = len(x_nodes)
        result = 0.0

        for i in range(n):
            term = y_nodes[i]
            for j in range(n):
                if i != j:
                    term *= (x_target - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            result += term

        return result

    def get_name(self) -> str:
        """Returns method name."""
        return "Lagrange"