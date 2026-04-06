"""
Funciones generales de valor presente esperado.
"""

from .utilidades import descuento_temporal


def valor_presente_flujos(flujos: list[tuple[float, float]], i: float) -> float:
    """
    flujos = [(tiempo, monto), ...]
    """
    vp = 0.0
    for tiempo, monto in flujos:
        vp += monto * descuento_temporal(i, tiempo)
    return vp


def valor_presente_esperado(pagos: list[tuple[float, float, float]], i: float) -> float:
    """
    pagos = [(tiempo, monto, probabilidad), ...]
    """
    vpe = 0.0
    for tiempo, monto, probabilidad in pagos:
        vpe += monto * probabilidad * descuento_temporal(i, tiempo)
    return vpe
