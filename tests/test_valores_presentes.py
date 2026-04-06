from funciones_actuariales.valores_presentes import (
    valor_presente_flujos,
    valor_presente_monto,
)


def test_valor_presente_monto():
    valor = valor_presente_monto(1000, 0.05, 2)
    assert valor > 0
    assert valor < 1000


def test_valor_presente_flujos():
    flujos = [100, 100, 100]
    valor = valor_presente_flujos(flujos, 0.05)
    assert valor > 0
