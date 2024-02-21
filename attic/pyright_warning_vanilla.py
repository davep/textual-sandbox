"""Trying to create non-Textual code that shows the same pyright errors as Textual does.

So far I'm failing.
"""

from typing import Generic, TypeVar, ClassVar, Any

T = TypeVar("T")


class WeWentDeeper(type):
    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        class_dict: dict[str, Any],
        **kwargs,
    ):
        return super().__new__(cls, name, bases, class_dict, **kwargs)


class VeryBaseMuchClass(metaclass=WeWentDeeper):

    VERY_BASSE: ClassVar[int] = 0


class ParentClass(Generic[T], VeryBaseMuchClass):

    @property
    def this_thing(self) -> "ParentClass[Any]":
        return self

    @staticmethod
    def static_passthrough(value: T) -> T:
        return value

    @classmethod
    def class_method_passthrough(cls, value: T) -> T:
        return value


class ChildClass(ParentClass[T]):
    pass


class MyImplementation(ChildClass[int]):
    pass
