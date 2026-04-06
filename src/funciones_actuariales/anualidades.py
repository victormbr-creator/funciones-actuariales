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
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x

    suma = 0.0
    for k in range(0, max_edad + 1):
        prob = 1.0 if k == 0 else tabla.npx(x, k)
        suma += descuento_temporal(i, k) * prob
    return suma


def anualidad_temporal_inmediata(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    a_x:n = sum_{k=1}^{n} v^k * k p_x
    """
    suma = 0.0
    for k in range(1, n + 1):
        suma += descuento_temporal(i, k) * tabla.npx(x, k)
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
        prob = 1.0 if k == 0 else tabla.npx(x, k)
        suma += descuento_temporal(i, k) * prob
    return suma


def anualidad_diferida(
    x: int,
    m: int,
    n: int,
    i: float,
    tabla: TablaMortalidad,
    anticipada: bool = True
) -> float:
    """
    Anualidad diferida m años y pagadera por n años.

    Si anticipada=True:
        {}_m|ä_x:n = sum_{k=m}^{m+n-1} v^k * k p_x

    Si anticipada=False:
        {}_m|a_x:n = sum_{k=m+1}^{m+n} v^k * k p_x
    """
    suma = 0.0

    if anticipada:
        for k in range(m, m + n):
            prob = 1.0 if k == 0 else tabla.npx(x, k)
            suma += descuento_temporal(i, k) * prob
    else:
        for k in range(m + 1, m + n + 1):
            suma += descuento_temporal(i, k) * tabla.npx(x, k)

    return suma
