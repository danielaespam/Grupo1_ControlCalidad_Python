from datetime import date
import re


class Analista:
    def __init__(self):
        self._codigo_empleado = None
        self._nombre = None
        self._fecha_inicio_muestra = None

    def get_codigo_empleado(self):
        return self._codigo_empleado

    def set_codigo_empleado(self, codigo_empleado):
        if not isinstance(codigo_empleado, str) or not re.fullmatch(r'QA-\d{2}', codigo_empleado):
            print('El codigo de empleado debe tener el formato QA-00')
            return
        self._codigo_empleado = codigo_empleado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            print('El nombre no puede estar vacio')
            return
        self._nombre = nombre

    def get_fecha_inicio_muestra(self):
        return self._fecha_inicio_muestra

    def set_fecha_inicio_muestra(self, fecha):
        try:
            if not isinstance(fecha, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fecha):
                raise ValueError
            date.fromisoformat(fecha)
        except ValueError:
            print('La fecha de inicio debe ser valida (yyyy-MM-dd)')
            return
        self._fecha_inicio_muestra = fecha
