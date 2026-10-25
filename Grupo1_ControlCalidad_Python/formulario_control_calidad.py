from datetime import date
import re


class FormularioControlCalidad:
    def __init__(self, fecha_produccion=None, lote=None):
        self._fecha_produccion = None
        self._lote = None
        self._analista = None
        self._muestras = None
        self._cerrado = False
        if fecha_produccion is not None:
            self.set_fecha_produccion(fecha_produccion)
        if lote is not None:
            self.set_lote(lote)

    def get_fecha_produccion(self):
        return self._fecha_produccion

    def set_fecha_produccion(self, fecha):
        try:
            if not isinstance(fecha, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fecha):
                raise ValueError
            date.fromisoformat(fecha)
        except ValueError:
            print('La fecha de produccion debe ser valida (yyyy-MM-dd)')
            return
        self._fecha_produccion = fecha

    def get_lote(self):
        return self._lote

    def set_lote(self, lote):
        if not isinstance(lote, str) or not re.fullmatch(r'L-\d{4}-[A-Z]', lote):
            print('El lote debe tener el formato L-0000-A')
            return
        self._lote = lote

    def get_analista(self):
        return self._analista

    def set_analista(self, analista):
        if (analista is None or analista.get_codigo_empleado() is None
                or analista.get_fecha_inicio_muestra() is None):
            print('El analista debe tener codigo de empleado y fecha de inicio de muestra')
            return
        self._analista = analista

    def is_cerrado(self):
        return self._cerrado

    def agregar_muestra(self, muestra):
        if self._fecha_produccion is None or self._lote is None:
            print('El formulario debe tener fecha de produccion y lote validos')
            return
        if self._analista is None:
            print('Debe asignar un analista antes de registrar muestras')
            return
        if self._cerrado:
            print('El formulario ya esta cerrado')
            return
        if muestra is None or muestra.get_producto() is None or not muestra.is_validada():
            print('La muestra debe tener producto y lectura de temperatura')
            return
        if self._muestras is None:
            self._muestras = []
        self._muestras.append(muestra)

    def get_muestras(self):
        if self._muestras is None:
            print('No hay muestras registradas')
            return None
        return self._muestras

    def contar_aptos(self):
        return sum(muestra.is_apto() for muestra in (self._muestras or []))

    def contar_no_aptos(self):
        return len(self._muestras or []) - self.contar_aptos()

    def cerrar_analisis(self):
        if self._fecha_produccion is None or self._lote is None:
            print('El formulario debe tener fecha de produccion y lote validos')
            return
        if self._analista is None:
            print('No se puede cerrar el analisis sin analista asignado')
            return
        if self._cerrado:
            print('El analisis ya fue cerrado')
            return
        self._cerrado = True
        print('===== BATCH SUMMARY =====')
        print(f'Lote: {self._lote} | Fecha produccion: {self._fecha_produccion}')
        print(f'Analista: {self._analista.get_nombre()} ({self._analista.get_codigo_empleado()})'
              f' | Inicio muestra: {self._analista.get_fecha_inicio_muestra()}')
        print(f'Total Muestras: {len(self._muestras or [])}')
        print(f'Aptos: {self.contar_aptos()}')
        print(f'No Aptos: {self.contar_no_aptos()}')
