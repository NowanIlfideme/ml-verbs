"""Interfaces, or 'verbs', for machine learning."""

__all__ = [
    "IInvertable",
    "ITrain",
    "ITransform",
    "IPredictContinuous",
    "IPredictCategorical",
    "IPredict",
    "__version__",
]

from .protocols import (
    IInvertable,
    IPredict,
    IPredictCategorical,
    IPredictContinuous,
    ITrain,
    ITransform,
)
from .version import __version__
