"""Generic protocols."""

from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable

TDataIn = TypeVar("TDataIn", contravariant=True)
TDataOut = TypeVar("TDataOut", covariant=True)
TTrainOut = TypeVar("TTrainOut", covariant=True)
TInvertOut = TypeVar("TInvertOut", covariant=True)


@runtime_checkable
class ITransform(Protocol[TDataIn, TDataOut]):
    """I transform data into some other data."""

    @abstractmethod
    def transform(self, data: TDataIn) -> TDataOut:
        """Tranform input data into output data."""


@runtime_checkable
class ITrain(Protocol[TDataIn, TTrainOut]):
    """I train something based on data given to me."""

    @abstractmethod
    def train(self, data: TDataIn) -> TTrainOut:
        """Train something based on the input data."""


@runtime_checkable
class IInvertable(Protocol[TInvertOut]):
    """I am invertable."""

    @abstractmethod
    def invert(self) -> TInvertOut:
        """Return the inverse of this object."""
