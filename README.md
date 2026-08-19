# Actividad 01 — Banco virtual de mediciones DC

## ¿Qué vas a construir?

Una aplicación sencilla en Python para registrar mediciones de una fuente nominal de **5 V**, calcular potencia, determinar si el voltaje está dentro del rango permitido y mostrar un resumen.

Al finalizar podrás ejecutar:

```text
BANCO VIRTUAL DE MEDICIONES DC
1. Registrar medición
2. Mostrar resumen
3. Salir
```

El programa deberá clasificar cada voltaje así:

- **BAJO**: menor que 4.75 V
- **NORMAL**: entre 4.75 V y 5.25 V, inclusive
- **ALTO**: mayor que 5.25 V

La actividad repasa:

- lenguajes compilados, de máquina virtual e interpretados;
- intérprete de Python y módulos;
- `bool`, `int`, `float`, `complex`, `str` y `list`;
- operadores;
- `if / elif / else`;
- `for`;
- `while`;
- `match / case`;
- funciones;
- variables globales y locales.

No necesitas instalar librerías externas.

---

# Antes de empezar — Python, intérprete y módulos

Esta parte es conceptual y dura pocos minutos.

Abre la terminal de VS Code y ejecuta:

```bash
python --version
```

Luego:

```bash
python
```

Deberás entrar al intérprete interactivo de Python. Sal con:

```python
exit()
```

Después comprueba que Python puede importar un módulo del proyecto:

```bash
python -c "import src.mediciones; print('Módulo cargado correctamente')"
```

Piensa antes de continuar:

1. ¿Python se ejecuta como C, Java o de una forma distinta?
2. ¿Qué es un módulo en Python?
3. ¿Qué archivo de este proyecto contiene constantes globales?

Cuando lo tengas claro, comienza la Etapa 1.

---

# Ruta de trabajo

## Etapa 1 — Tipos de datos y operadores

Abre:

```text
src/mediciones.py
```

Completa únicamente:

```python
crear_medicion(...)
calcular_potencia(...)
```

### 1. Crear una medición

Una medición se representará como una lista con seis datos:

```python
[
    1,          # int: número de muestra
    "TP1",     # str: punto de prueba
    5.02,       # float: voltaje
    0.20,       # float: corriente
    True,       # bool: equipo activo
    10 + 2j     # complex: impedancia de prueba
]
```

La función `crear_medicion(...)` debe retornar esos seis datos en ese mismo orden.

### 2. Calcular potencia

Usa:

```text
P = V × I
```

Ejemplo:

```python
calcular_potencia(5.0, 0.2)
```

debe retornar:

```text
1.0
```

### Comprobar la etapa

Ejecuta:

```bash
python scripts/revisar_progreso.py
```

El sistema te dirá si puedes avanzar.

---

## Etapa 2 — Condicionales

Completa:

```python
clasificar_voltaje(voltaje)
```

Debes usar obligatoriamente:

```python
if
elif
else
```

Reglas:

```text
voltaje < 4.75      → BAJO
4.75 <= voltaje <= 5.25 → NORMAL
voltaje > 5.25      → ALTO
```

Ejemplos:

```python
clasificar_voltaje(4.50)  # "BAJO"
clasificar_voltaje(5.00)  # "NORMAL"
clasificar_voltaje(5.40)  # "ALTO"
```

Después ejecuta:

```bash
python scripts/revisar_progreso.py
```

---

## Etapa 3 — Listas y ciclos

Completa estas funciones:

```python
calcular_promedio(voltajes)
contar_fuera_rango(voltajes)
buscar_primero_normal(voltajes)
```

### Promedio

Para:

```python
[5.0, 4.5, 5.1, 5.4]
```

debes recorrer la lista con `for` y calcular el promedio.

Si la lista está vacía, retorna `0.0`.

### Contar valores fuera de rango

Usa `for` para contar cuántos voltajes están clasificados como `BAJO` o `ALTO`.

### Buscar el primer voltaje normal

Usa obligatoriamente `while`.

Ejemplo:

```python
buscar_primero_normal([4.0, 4.6, 5.1, 5.3])
```

debe retornar:

```text
5.1
```

Si ninguno está dentro del rango, retorna `None`.

Después ejecuta:

```bash
python scripts/revisar_progreso.py
```

---

## Etapa 4 — Funciones e integración

Completa:

```python
generar_resumen(voltajes)
```

Esta función debe reutilizar las funciones anteriores y retornar:

```python
[promedio, cantidad_fuera_de_rango, primer_voltaje_normal]
```

Ejemplo:

```python
generar_resumen([4.0, 5.0, 5.1])
```

Resultado esperado:

```python
[4.7, 1, 5.0]
```

Después abre:

```text
src/app.py
```

Completa `ejecutar()`.

La aplicación debe:

1. mantener el menú activo usando `while`;
2. procesar las opciones usando `match / case`;
3. permitir registrar voltajes;
4. mostrar el resumen;
5. salir con la opción `0`.

No necesitas crear una interfaz gráfica.

---

# ¿Cómo revisar tu avance?

Usa siempre:

```bash
python scripts/revisar_progreso.py
```

Este comando **no muestra todas las fallas del proyecto de una vez**. Revisa una etapa por vez y se detiene en la primera que todavía necesita trabajo.

Cuando todas las etapas estén correctas, prueba la aplicación:

```bash
python -m src.app
```

---

# Tutor de IA

En GitHub Copilot Chat selecciona:

**Tutor Fundamentos Python**

Puedes comenzar con:

> Revisa mi progreso. No modifiques ningún archivo.

El tutor debe:

1. ejecutar la revisión real del proyecto;
2. explicarte en qué etapa estás;
3. decirte exactamente qué función debes trabajar;
4. darte inicialmente una sola pista;
5. aumentar el nivel de ayuda solo si lo necesitas.

La IA está para ayudarte a aprender, no para completar automáticamente toda la actividad.

---

# Commits sugeridos

Cuando termines cada etapa:

```text
etapa 1: tipos y operadores
etapa 2: condicionales
etapa 3: listas y ciclos
etapa 4: integracion de la aplicacion
```

---

# Entrega

Antes de entregar:

```bash
python scripts/revisar_progreso.py
```

Debe mostrar que todas las etapas fueron superadas.

Después completa `PROGRESO.md` y realiza el commit final.
