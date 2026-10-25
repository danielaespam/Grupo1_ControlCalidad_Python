import unittest

from analista import Analista
from formulario_control_calidad import FormularioControlCalidad
from muestra import Muestra
from producto import Producto
from sonda_temperatura import SondaTemperatura


class TestControlCalidad(unittest.TestCase):
    def test_limite_temperatura(self):
        muestra = Muestra()
        muestra.set_producto(Producto('ATUN', 'ALBACORA'))
        muestra.set_temperatura(4.0)
        self.assertEqual(muestra.get_resultado(), 'APTO')
        muestra.set_temperatura(4.1)
        self.assertEqual(muestra.get_resultado(), 'NO APTO')

    def test_sonda_no_calibrada(self):
        self.assertIsNone(SondaTemperatura().leer_temperatura())

    def test_formulario_con_cierre(self):
        formulario = FormularioControlCalidad('2026-10-14', 'L-2026-A')
        analista = Analista()
        analista.set_codigo_empleado('QA-02')
        analista.set_nombre('Maria Lopez')
        analista.set_fecha_inicio_muestra('2026-10-14')
        formulario.set_analista(analista)
        muestra = Muestra()
        muestra.set_producto(Producto('ATUN', 'ALBACORA'))
        muestra.set_temperatura(3.2)
        formulario.agregar_muestra(muestra)
        self.assertEqual(formulario.contar_aptos(), 1)
        self.assertEqual(formulario.contar_no_aptos(), 0)
        formulario.cerrar_analisis()
        self.assertTrue(formulario.is_cerrado())
        formulario.agregar_muestra(muestra)
        self.assertEqual(len(formulario.get_muestras()), 1)

    def test_codigo_invalido(self):
        analista = Analista()
        analista.set_codigo_empleado('INCORRECTO')
        self.assertIsNone(analista.get_codigo_empleado())


if __name__ == '__main__':
    unittest.main()
