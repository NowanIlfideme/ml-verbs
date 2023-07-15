"""Protocol definitions."""

__all__ = [
    "IInvertable",
    "ITrain",
    "ITransform",
    "IPredictContinuous",
    "IPredictCategorical",
    "IPredict",
]

from .generic import IInvertable, ITrain, ITransform
from .xy import IPredict, IPredictCategorical, IPredictContinuous
