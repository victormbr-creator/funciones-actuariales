from funciones_actuariales.tablas import TablaMortalidad
from funciones_actuariales.anualidades import anualidad_temporal_anticipada
from funciones_actuariales.seguros import seguro_temporal

# Creamos una tabla de mortalidad
datos_lx = {
    0: 1000,
    1: 900,
    2: 800,
    3: 700,
    4: 600,
    5: 500,
}

tabla = TablaMortalidad(datos_lx)

# Parámetros
edad = 0
tasa = 0.05
n = 3

# Cálculos
anualidad = anualidad_temporal_anticipada(edad, n, tasa, tabla)
seguro = seguro_temporal(edad, n, tasa, tabla)

print("Anualidad:", anualidad)
print("Seguro:", seguro)
