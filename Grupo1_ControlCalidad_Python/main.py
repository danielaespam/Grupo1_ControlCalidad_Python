from analista import Analista
from formulario_control_calidad import FormularioControlCalidad
from muestra import Muestra
from producto import Producto
from sonda_temperatura import SondaTemperatura


def main():
    # Paso 1: Recepcion del lote
    formulario1 = FormularioControlCalidad('2026-10-14', 'L-2026-A')

    # Paso 2: Asignacion del analista
    analista1 = Analista()
    analista1.set_codigo_empleado('QA-02')
    analista1.set_nombre('Maria Lopez')
    analista1.set_fecha_inicio_muestra('2026-10-14')
    formulario1.set_analista(analista1)

    producto1 = Producto('ATUN', 'ALBACORA 70 - 120 Lb')

    # Paso 3: Preparacion de la sonda
    sonda1 = SondaTemperatura()
    sonda1.set_codigo('SONDA-01')
    sonda1.set_calibrada(True)

    # Pasos 3 y 4: Analisis de 15 pescados
    for i in range(1, 16):
        muestra = Muestra()
        muestra.set_producto(producto1)
        muestra.set_temperatura(sonda1.leer_temperatura())
        print(f'Muestra {i}: {muestra.get_producto().get_nombre()}, '
              f'Temp: {muestra.get_temperatura()} °C, Resultado: {muestra.get_resultado()}')
        formulario1.agregar_muestra(muestra)

    # Paso 5: Balance del lote
    formulario1.cerrar_analisis()


if __name__ == '__main__':
    main()
