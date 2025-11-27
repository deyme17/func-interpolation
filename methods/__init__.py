from .interpolation_method import IInterpolationMethod
from .lagrange_interpolation import LagrangeInterpolation
from .newton_interpolation import NewtonInterpolation

interpolation_methods: dict[str, IInterpolationMethod] = {
    "Newton": NewtonInterpolation(),
    "Lagrange": LagrangeInterpolation()
}