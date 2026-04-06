from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.conmutacion import Dx, Nx, Cx, Mx, Rx


def crear_tabla_prueba():
    datos_lx = {
        0: 1000,
        1: 900,
        2: 800,
        3: 700,
        4: 600,
        5: 500,
    }
    return TablaMortalidad(datos_lx)


def test_Dx():
    tabla = crear_tabla_prueba()
    valor = Dx(2, 0.05, tabla)
    assert valor > 0


def test_Nx():
    tabla = crear_tabla_prueba()
    valor = Nx(2, 0.05, tabla)
    assert valor > 0


def test_Cx():
    tabla = crear_tabla_prueba()
    valor = Cx(2, 0.05, tabla)
    assert valor > 0


def test_Mx():
    tabla = crear_tabla_prueba()
    valor = Mx(2, 0.05, tabla)
    assert valor > 0


def test_Rx():
    tabla = crear_tabla_prueba()
    valor = Rx(2, 0.05, tabla)
    assert valor > 0
