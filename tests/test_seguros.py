from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.seguros import seguro_temporal


def test_seguro_temporal():
    tabla = TablaMortalidad({
        40: 100000,
        41: 99000,
        42: 97500,
        43: 95000,
        44: 92000,
    })
    resultado = seguro_temporal(40, 3, 0.04, tabla)
    assert resultado > 0
