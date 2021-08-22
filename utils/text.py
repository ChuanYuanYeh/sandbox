"""
    This file contains functions dealing with strings.
"""


def to_snake_case(x: str) -> str:
    lowered = x.lower().replace(' ', '_')
    return lowered