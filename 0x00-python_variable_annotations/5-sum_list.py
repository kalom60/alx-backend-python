#!/usr/bin/env python3
"""Complex types - list of floats """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """returns input_list sum as a float"""
    return float(sum(input_list))
