"""
Clases para tablas de mortalidad.
"""


class TablaMortalidad:
    def __init__(self, datos_lx: dict):
        self.datos_lx = datos_lx

    def lx(self, x: int) -> float:
        if x not in self.datos_lx:
            raise ValueError(f"No existe l_{x} en la tabla.")
        return self.datos_lx[x]

    def dx(self, x: int) -> float:
        if x not in self.datos_lx:
            raise ValueError(f"No existe l_{x} en la tabla.")
        if x + 1 in self.datos_lx:
            return self.datos_lx[x] - self.datos_lx[x + 1]
        return self.datos_lx[x]

    def npx(self, x: int, n: int) -> float:
        if x not in self.datos_lx or x + n not in self.datos_lx:
            return 0.0
        if self.datos_lx[x] == 0:
            return 0.0
        return self.datos_lx[x + n] / self.datos_lx[x]

    def nqx(self, x: int, n: int) -> float:
        if x not in self.datos_lx or x + n not in self.datos_lx:
            return 0.0
        if self.datos_lx[x] == 0:
            return 0.0
        if x + n + 1 in self.datos_lx:
            return (self.datos_lx[x + n] - self.datos_lx[x + n + 1]) / self.datos_lx[x]
        return self.datos_lx[x + n] / self.datos_lx[x]
