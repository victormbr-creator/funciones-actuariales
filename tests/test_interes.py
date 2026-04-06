from funciones_actuariales.interes import factor_descuento, tasa_descuento


def test_factor_descuento():
    assert round(factor_descuento(0.05), 6) == round(1 / 1.05, 6)


def test_tasa_descuento():
    assert round(tasa_descuento(0.05), 6) == round(0.05 / 1.05, 6)
