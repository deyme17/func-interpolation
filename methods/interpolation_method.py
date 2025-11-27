from abc import ABC, abstractmethod
import numpy as np

class IInterpolationMethod(ABC):
    """Interface class for interpolation strategies."""
    @abstractmethod
    def interpolate(self, x_nodes: np.ndarray, y_nodes: np.ndarray, x_target: float) -> float:
        """Calculates the interpolated value at a specific point."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Returns the display name of the method."""
        pass