#!/usr/bin/env python3
"""Module to compute square root"""


def sqrt(num: float) -> float:
    """function to compute square root"""
    if num < 0:
        return ValueError('number must be greater than 0')
    return (num ** 0.5)
