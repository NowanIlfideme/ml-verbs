"""Protocols for cross-sectional problems."""

from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable

TDataIn = TypeVar("TDataIn", contravariant=True)
TDataOut = TypeVar("TDataOut", covariant=True)


@runtime_checkable
class IPredict(Protocol[TDataIn, TDataOut]):
    """I predict something based on data."""

    @abstractmethod
    def predict(self, data: TDataIn) -> TDataOut:
        """Predict an output based on the data."""


@runtime_checkable
class IPredictCategorical(IPredict[TDataIn, TDataOut], Protocol[TDataIn, TDataOut]):
    """I predict categorical values based on data."""

    @abstractmethod
    def predict_categorical(self, data: TDataIn) -> TDataOut:
        """Predict a category based on the data."""

    def predict(self, data: TDataIn) -> TDataOut:
        """Predict a category based on the data."""
        return self.predict_categorical(data)


@runtime_checkable
class IPredictContinuous(IPredict[TDataIn, TDataOut], Protocol[TDataIn, TDataOut]):
    """I predict continuous values based on data."""

    @abstractmethod
    def predict_continuous(self, data: TDataIn) -> TDataOut:
        """Predict a continuous value based on the data."""

    def predict(self, data: TDataIn) -> TDataOut:
        """Predict a continuous value based on the data."""
        return self.predict_continuous(data)
