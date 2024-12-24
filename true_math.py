# true_math.py
from math import inf


def divide(first, second):
    """Деление с возвращением бесконечности при делении на 0."""
    if second == 0:
        return inf
    return first / second
