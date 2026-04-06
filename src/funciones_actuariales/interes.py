"""
Funciones financieras básicas para matemática actuarial.
Todas las funciones están escritas en español.
"""

def factor_descuento(i: float) -> float:
    """
    Devuelve v = 1 / (1 + i)
    """
    if i <= -1:
        raise ValueError("La tasa de interés i debe ser mayor que -1.")
    return 1 / (1 + i)


def tasa_descuento(i: float) -> float:
    """
    Devuelve d = i / (1 + i)
    """
    if i <= -1:
        raise ValueError("La tasa de interés i debe ser mayor que -1.")
    return i / (1 + i)


def fuerza_interes(i: float) -> float:
    """
    Devuelve delta = ln(1 + i)
    """
    import math
    if i <= -1:
        raise ValueError("La tasa de interés i debe ser mayor que -1.")
    return math.log(1 + i)


def valor_presente(monto: float, i: float, t: float) -> float:
    """
    Calcula el valor presente de un monto a pagar en t periodos:
    VP = monto / (1+i)^t
    """
    if monto < 0:
        raise ValueError("El monto no puede ser negativo.")
    if i <= -1:
        raise ValueError("La tasa de interés i debe ser mayor que -1.")
    return monto / ((1 + i) ** t)


def valor_futuro(monto: float, i: float, t: float) -> float:
    """
    Calcula el valor futuro de un monto invertido durante t periodos:
    VF = monto * (1+i)^t
    """
    if monto < 0:
        raise ValueError("El monto no puede ser negativo.")
    if i <= -1:
        raise ValueError("La tasa de interés i debe ser mayor que -1.")
    return monto * ((1 + i) ** t)
