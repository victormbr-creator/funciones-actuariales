"""
Funciones para anualidades actuariales.
"""

from typing import Optional
from .utilidades import descuento_temporal
from .tablas import TablaMortalidad


def anualidad_vitalicia_inmediata(
    x: int,
    i: float,
    tabla: TablaMortalidad,
    max_edad: Optional[int] = None
) -> float:
    """
    a_x = sum_{k>=1} v^k * k p_x
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x

    suma = 0.0
    for k in range(1, max_edad + 1):
        suma += descuento_temporal(i, k) * tabla.npx(x, k)
    return suma


def anualidad_vitalicia_anticipada(
    x: int,
    i: float,
    tabla: TablaMortalidad,
    max_edad: Optional[int] = None
) -> float:
    """
    ä_x = sum_{k>=0} v^k * k p_x
    donde 0 p_x = 1
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x

    suma = 0.0
    for k in range(0, max_edad + 1):
        if k == 0:
            prob = 1.0
        else:
            prob = tabla.npx(x, k)

        suma += descuento_temporal(i, k) * prob

    return suma


def anualidad_temporal_anticipada(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    ä_x:n = sum_{k=0}^{n-1} v^k * k p_x
    """
    suma = 0.0
    for k in range(0, n):
        if k == 0:
            prob = 1.0
        else:
            prob = tabla.npx(x, k)

        suma += descuento_temporal(i, k) * prob

    return suma
