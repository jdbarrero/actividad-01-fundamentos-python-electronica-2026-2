# Configuración docente

## Objetivo

Publicar este repositorio como plantilla de GitHub para que cada estudiante o grupo cree su propia copia.

## Publicación inicial

1. Crea un repositorio vacío en GitHub, por ejemplo:

   `actividad-01-banco-mediciones-dc`

2. Desde esta carpeta ejecuta:

```bash
git init
git add .
git commit -m "Actividad 01: banco virtual de mediciones DC"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

3. En GitHub entra a `Settings > General`.
4. Activa `Template repository`.

## Prueba como estudiante

1. Usa `Use this template`.
2. Crea una copia de prueba.
3. Clónala en VS Code.
4. Selecciona `Tutor Fundamentos Python` en Copilot Chat.
5. Escribe:

   `Revisa mi progreso. No modifiques ningún archivo.`

El agente debe ejecutar `python scripts/revisar_progreso.py` y detenerse en la primera etapa pendiente.

## Comportamiento esperado

El tutor no debe mostrar decenas de fallas a la vez. Debe explicar:

- qué construye el estudiante;
- cuál es la etapa actual;
- qué archivo abrir;
- qué función trabajar;
- una pista inicial.

GitHub Actions sí ejecutará todas las pruebas al hacer `push`.
