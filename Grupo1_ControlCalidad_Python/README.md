# Grupo 1 - Control de Calidad (Python)

Migración a **Python 3.10+** del proyecto de la Hackatón POO, originalmente desarrollado en Java por el Grupo 1.

## Descripción

Sistema orientado a objetos para registrar un lote de pescado, asignar un analista, simular la lectura de temperatura de 15 muestras mediante una sonda calibrada y obtener un balance final de muestras **APTAS** (temperatura <= 4.0 °C) y **NO APTAS** (temperatura > 4.0 °C).

## Requisitos

- Python 3.10 o posterior.
- No necesita instalar bibliotecas externas.

## Ejecución

1. Descarga o clona este repositorio.
2. Abre una terminal dentro de la carpeta que contiene `main.py`.
3. Ejecuta:

   **Windows:**

   ```bash
   py main.py
   ```

   **macOS / Linux:**

   ```bash
   python3 main.py
   ```

Si `py` no está disponible en Windows, prueba `python main.py`.

El sistema imprimirá la temperatura y el resultado de cada una de las 15 muestras, seguido por un resumen del lote. Las temperaturas se **simulan aleatoriamente**, por lo que el número de muestras aptas puede variar entre ejecuciones.

## Estructura del proyecto

| Archivo | Responsabilidad |
|---|---|
| `analista.py` | Datos y validación del analista |
| `producto.py` | Datos y validación del producto |
| `sonda_temperatura.py` | Calibración y simulación de temperaturas |
| `muestra.py` | Validación y clasificación de cada muestra |
| `formulario_control_calidad.py` | Registro, conteo y cierre del lote |
| `main.py` | Ejemplo completo de ejecución |
| `tests/test_control_calidad.py` | Pruebas automatizadas básicas |

## Pruebas

Desde la carpeta del proyecto ejecuta:

```bash
python -m unittest discover -s tests -v
```

En Windows también puedes utilizar `py -m unittest discover -s tests -v`.

## Migración de Java a Python

- Se conservaron las **seis clases** y sus responsabilidades.
- Se adaptaron los métodos al estilo `snake_case` habitual de Python.
- Se preservaron las validaciones de fechas, códigos, lote, analista y sonda calibrada.
- Se mantuvo el límite de temperatura de **4.0 °C**.
- Se mantiene el cierre del formulario, que impide agregar nuevas muestras.
- La lista de muestras usa `list` en lugar de `ArrayList`.
- `random.random()` reemplaza a `Math.random()` para simular lecturas.

**Nota:** las mediciones son una simulación didáctica; no sustituyen lecturas de equipos reales ni procedimientos técnicos de inocuidad alimentaria.

## Origen

Proyecto de Java: [HackathonPOO-ControlCalidad-main, Grupo1](https://github.com/danielaespam/HackathonPOO-ControlCalidad-main/tree/main/HackathonPOO-ControlCalidad-main/Grupo1).
