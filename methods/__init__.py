from .interpolation_method import IInterpolationMethod
from .lagrange_interpolation import LagrangeInterpolation
from .newton_interpolation import NewtonInterpolation

interpolation_methods: dict[str, IInterpolationMethod] = {
    NewtonInterpolation().get_name(): NewtonInterpolation(),
    LagrangeInterpolation().get_name(): LagrangeInterpolation()
}