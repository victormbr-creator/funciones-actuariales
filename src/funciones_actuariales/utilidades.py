"""
Funciones auxiliares.
"""

from .interes import factor_descuento


def descuento_temporal(i: float, t: float) -> float:
    """
    Devuelve v^t
    """
    v = factor_descuento(i)
    return v ** t
