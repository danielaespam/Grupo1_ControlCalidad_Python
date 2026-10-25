import random


class SondaTemperatura:
    def __init__(self):
        self._codigo = None
        self._calibrada = False

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            print('El codigo de la sonda no puede estar vacio')
            return
        self._codigo = codigo

    def is_calibrada(self):
        return self._calibrada

    def set_calibrada(self, calibrada):
        self._calibrada = bool(calibrada)

    def leer_temperatura(self):
        if not self._calibrada:
            print('La sonda no esta calibrada')
            return None
        # Lectura simulada entre 0.0 y 5.0 °C, redondeada a un decimal.
        return round(random.random() * 5.0, 1)
