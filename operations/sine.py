#!/usr/bin/env python3
"""
This module includes the implementation of a sine function
"""
import math
from typing import Union


def sine(angle: float) -> float:
    """
    Calculate the sine of angle in degrees.

    Prameters:
    angle (float): The angle in degrees.

    Returns:
    float: The sine of the angle.
    """
    # Converts the value from degrees to radians
    value_in_radians = math.radians(angle)

    return math.sin(value_in_radians)
