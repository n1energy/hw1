from typing import Any
import itertools

__all__ = ("cartesian_product",)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    return list(itertools.product(arr1, arr2))
