"""
Funciones para seguros actuariales.
"""

from typing import Optional
from .utilidades import descuento_temporal
from .tablas import TablaMortalidad


def seguro_vitalicio(x: int, i: float, tabla: TablaMortalidad, max_edad: Optional[int] = None) -> float:
    """
    A_x = sum_{k>=0} v^(k+1) * k p_x * q_{x+k}
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x - 1

    suma = 0.0
    for k in range(0, max_edad + 1):
        suma += descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_temporal(x: int, n: int, i: float, tabla: TablaMortalidad) -> float:
    """
    A_{x:n} = sum_{k=0}^{n-1} v^(k+1) * k p_x * q_{x+k}
    """
    suma = 0.0
    for k in range(0, n):
        suma += descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_diferido(x: int, n: int, m: int, i: float, tabla: TablaMortalidad) -> float:
    """
    Seguro temporal n años, diferido m años.
    """
    suma = 0.0
    for k in range(m, m + n):
        suma += descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_vitalicio_diferido(x: int, m: int, i: float, tabla: TablaMortalidad, max_edad: Optional[int] = None) -> float:
    """
    Seguro vitalicio diferido m años.
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x - 1

    suma = 0.0
    for k in range(m, max_edad + 1):
        suma += descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_creciente(x: int, n: int, i: float, tabla: TablaMortalidad) -> float:
    """
    Beneficio k+1 en el año k+1 si ocurre fallecimiento.
    """
    suma = 0.0
    for k in range(0, n):
        suma += (k + 1) * descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_decreciente(x: int, n: int, i: float, tabla: TablaMortalidad) -> float:
    """
    Beneficio n-k en el año k+1 si ocurre fallecimiento.
    """
    suma = 0.0
    for k in range(0, n):
        suma += (n - k) * descuento_temporal(i, k + 1) * tabla.npx(x, k) * tabla.qx(x + k)
    return suma


def seguro_dotal(x: int, n: int, i: float, tabla: TablaMortalidad) -> float:
    """
    Seguro dotal puro + seguro temporal.
    """
    seguro_muerte = seguro_temporal(x, n, i, tabla)
    dotal_puro = descuento_temporal(i, n) * tabla.npx(x, n)
    return seguro_muerte + dotal_puro


def dotal_puro(x: int, n: int, i: float, tabla: TablaMortalidad) -> float:
    """
    {}_nE_x = v^n * n p_x
    """
    return descuento_temporal(i, n) * tabla.npx(x, n)
