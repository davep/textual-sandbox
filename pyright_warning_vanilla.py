"""Trying to create non-Textual code that shows the same pyright errors as Textual does.

So far I'm failing.
"""

from typing import Generic, TypeVar

T = TypeVar("T")

class ParentClass(Generic[T]):

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
