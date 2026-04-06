"""
Funciones para seguros actuariales.
"""

from typing import Optional
from .utilidades import descuento_temporal
from .tablas import TablaMortalidad


def seguro_vitalicio(
    x: int,
    i: float,
    tabla: TablaMortalidad,
    max_edad: Optional[int] = None
) -> float:
    """
    A_x = sum_{k>=0} v^{k+1} * k|q_x
    """
    if max_edad is None:
        max_edad = max(tabla.datos_lx.keys()) - x

    suma = 0.0
    for k in range(0, max_edad + 1):
        suma += descuento_temporal(i, k + 1) * tabla.nqx(x, k)
    return suma


def seguro_temporal(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    A_x:n = sum_{k=0}^{n-1} v^{k+1} * k|q_x
    """
    suma = 0.0
    for k in range(0, n):
        suma += descuento_temporal(i, k + 1) * tabla.nqx(x, k)
    return suma


def seguro_diferido(
    x: int,
    m: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    Seguro temporal diferido m años y pagadero por n años después del diferimiento.

    {}_m|A_x:n = sum_{k=m}^{m+n-1} v^{k+1} * k|q_x
    """
    suma = 0.0
    for k in range(m, m + n):
        suma += descuento_temporal(i, k + 1) * tabla.nqx(x, k)
    return suma


def seguro_dotal(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    Seguro dotal discreto:
    paga 1 al final del año de fallecimiento si ocurre dentro de n años,
    o 1 al final de n años si sobrevive.

    = A_x:n + v^n * n p_x
    """
    parte_seguro = seguro_temporal(x, n, i, tabla)
    parte_supervivencia = descuento_temporal(i, n) * tabla.npx(x, n)
    return parte_seguro + parte_supervivencia


def seguro_creciente(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    Seguro temporal creciente discreto:
    paga k+1 si la muerte ocurre en el año k+1.
    """
    suma = 0.0
    for k in range(0, n):
        suma += (k + 1) * descuento_temporal(i, k + 1) * tabla.nqx(x, k)
    return suma


def seguro_decreciente(
    x: int,
    n: int,
    i: float,
    tabla: TablaMortalidad
) -> float:
    """
    Seguro temporal decreciente discreto:
    paga n-k si la muerte ocurre en el año k+1.
    """
    suma = 0.0
    for k in range(0, n):
        suma += (n - k) * descuento_temporal(i, k + 1) * tabla.nqx(x, k)
    return suma
