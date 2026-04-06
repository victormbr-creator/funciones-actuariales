from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.seguros import (
    seguro_temporal,
    seguro_vitalicio,
    seguro_diferido,
    seguro_dotal,
    seguro_creciente,
    seguro_decreciente,
)


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


def test_seguro_temporal():
    tabla = crear_tabla_prueba()
    valor = seguro_temporal(0, 3, 0.05, tabla)
    assert valor > 0


def test_seguro_vitalicio():
    tabla = crear_tabla_prueba()
    valor = seguro_vitalicio(0, 0.05, tabla)
    assert valor > 0


def test_seguro_diferido():
    tabla = crear_tabla_prueba()
    valor = seguro_diferido(0, 1, 3, 0.05, tabla)
    assert valor > 0


def test_seguro_dotal():
    tabla = crear_tabla_prueba()
    valor = seguro_dotal(0, 3, 0.05, tabla)
    assert valor > 0


def test_seguro_creciente():
    tabla = crear_tabla_prueba()
    valor = seguro_creciente(0, 3, 0.05, tabla)
    assert valor > 0


def test_seguro_decreciente():
    tabla = crear_tabla_prueba()
    valor = seguro_decreciente(0, 3, 0.05, tabla)
    assert valor > 0
