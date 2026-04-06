"""
Funciones de conmutación actuarial.
"""

from .tablas import TablaMortalidad
from .utilidades import descuento_temporal


def Dx(x: int, i: float, tabla: TablaMortalidad) -> float:
    """
    D_x = v^x * l_x
    """
    lx = tabla.lx(x)
    return descuento_temporal(i, x) * lx


def Nx(x: int, i: float, tabla: TablaMortalidad) -> float:
    """
    N_x = sum_{k >= x} D_k
    """
    edades = sorted(tabla.datos_lx.keys())
    suma = 0.0
    for edad in edades:
        if edad >= x:
            suma += Dx(edad, i, tabla)
    return suma


def Cx(x: int, i: float, tabla: TablaMortalidad) -> float:
    """
    C_x = v^(x+1) * d_x
    """
    dx = tabla.dx(x)
    return descuento_temporal(i, x + 1) * dx


def Mx(x: int, i: float, tabla: TablaMortalidad) -> float:
    """
    M_x = sum_{k >= x} C_k
    """
    edades = sorted(tabla.datos_lx.keys())
    suma = 0.0
    for edad in edades:
        if edad >= x:
            suma += Cx(edad, i, tabla)
    return suma


def Rx(x: int, i: float, tabla: TablaMortalidad) -> float:
    """
    R_x = sum_{k >= x} M_k
    """
    edades = sorted(tabla.datos_lx.keys())
    suma = 0.0
    for edad in edades:
        if edad >= x:
            suma += Mx(edad, i, tabla)
    return suma
