from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.anualidades import anualidad_temporal_anticipada


def test_anualidad_temporal_anticipada():
    tabla = TablaMortalidad({
        30: 100000,
        31: 99000,
        32: 98000,
        33: 97000,
        34: 96000,
    })
    resultado = anualidad_temporal_anticipada(30, 3, 0.05, tabla)
    assert resultado > 0
