from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.anualidades import (
    anualidad_temporal_anticipada,
    anualidad_temporal_inmediata,
    anualidad_diferida,
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


def test_anualidad_temporal_anticipada():
    tabla = crear_tabla_prueba()
    valor = anualidad_temporal_anticipada(0, 3, 0.05, tabla)
    assert valor > 0


def test_anualidad_temporal_inmediata():
    tabla = crear_tabla_prueba()
    valor = anualidad_temporal_inmediata(0, 3, 0.05, tabla)
    assert valor > 0


def test_anualidad_diferida():
    tabla = crear_tabla_prueba()
    valor = anualidad_diferida(0, 1, 3, 0.05, tabla)
    assert valor > 0
