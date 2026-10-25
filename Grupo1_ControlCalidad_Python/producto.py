class Producto:
    def __init__(self, especie, nombre):
        self._especie = None
        self._nombre = None
        self.set_especie(especie)
        self.set_nombre(nombre)

    def get_especie(self):
        return self._especie

    def set_especie(self, especie):
        if not isinstance(especie, str) or not especie.strip():
            print('La especie no puede estar vacia')
            return
        self._especie = especie

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            print('El nombre no puede estar vacio')
            return
        self._nombre = nombre
