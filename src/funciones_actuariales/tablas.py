"""
Herramientas para tablas de mortalidad.
"""

class TablaMortalidad:
    def __init__(self, datos_lx: dict[int, float]):
        """
        datos_lx: diccionario con forma {edad: l_x}
        """
        if not datos_lx:
            raise ValueError("La tabla no puede estar vacía.")

        self.datos_lx = dict(sorted(datos_lx.items()))

    def lx(self, x: int) -> float:
        if x not in self.datos_lx:
            raise ValueError(f"No existe l_{x} en la tabla.")
        return self.datos_lx[x]

    def dx(self, x: int) -> float:
        if x + 1 not in self.datos_lx:
            raise ValueError(f"No existe l_{x+1} en la tabla.")
        return self.lx(x) - self.lx(x + 1)

    def qx(self, x: int) -> float:
        lx = self.lx(x)
        if lx == 0:
            raise ValueError(f"l_{x} no puede ser 0.")
        return self.dx(x) / lx

    def px(self, x: int) -> float:
        return 1 - self.qx(x)

    def npx(self, x: int, n: int) -> float:
        if x + n not in self.datos_lx:
            raise ValueError(f"No existe l_{x+n} en la tabla.")
        lx = self.lx(x)
        if lx == 0:
            raise ValueError(f"l_{x} no puede ser 0.")
        return self.lx(x + n) / lx

    def nqx(self, x: int, n: int) -> float:
        return 1 - self.npx(x, n)
