from abc import ABC, abstractmethod
from typing import Any, Optional, Type, TypeVar, Union

from pydantic import BaseConfig
from pydantic.fields import ModelField

T = TypeVar("T")


class AbstractTyping(ABC):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    @abstractmethod
    def validate(
        cls: Type[T],
        value: Union[Any, Any, Any],
        field: Optional['ModelField'] = None,
        config: Optional['BaseConfig'] = None,
    ) -> T:
        ...

    @classmethod
    @abstractmethod
    def from_protobuf(cls: Type[T], pb_msg: T) -> T:
        ...
