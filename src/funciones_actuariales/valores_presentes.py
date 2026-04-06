"""
Funciones generales de valor presente actuarial y financiero.
"""

from .utilidades import descuento_temporal


def valor_presente_flujos(flujos: list, i: float) -> float:
    """
    Calcula el valor presente de una lista de flujos.
    El flujo en la posición t se descuenta t periodos.
    """
    suma = 0.0
    for t, flujo in enumerate(flujos):
        suma += flujo * descuento_temporal(i, t)
    return suma


def valor_presente_monto(monto: float, i: float, n: int) -> float:
    """
    Valor presente de un monto único pagadero en n periodos.
    """
    return monto * descuento_temporal(i, n)
