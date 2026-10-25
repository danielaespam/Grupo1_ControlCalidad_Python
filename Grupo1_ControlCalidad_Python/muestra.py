class Muestra:
    TEMPERATURA_MAXIMA = 4.0

    def __init__(self):
        self._producto = None
        self._temperatura = None
        self._apto = None

    def get_producto(self):
        return self._producto

    def set_producto(self, producto):
        if producto is None:
            print('El producto no puede estar vacio')
            return
        self._producto = producto

    def get_temperatura(self):
        return self._temperatura

    def set_temperatura(self, temperatura):
        if temperatura is None:
            print('La temperatura no puede estar vacia')
            return
        self._temperatura = temperatura
        self.validar_condicion()

    def is_apto(self):
        return self._apto is True

    def is_validada(self):
        return self._apto is not None

    def validar_condicion(self):
        if self._temperatura is None:
            print('No se puede validar una muestra sin temperatura')
            return False
        self._apto = self._temperatura <= self.TEMPERATURA_MAXIMA
        return self._apto

    def get_resultado(self):
        if self._apto is None:
            return 'SIN LECTURA'
        return 'APTO' if self._apto else 'NO APTO'
