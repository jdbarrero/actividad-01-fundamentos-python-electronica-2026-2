"""Aplicación de consola del banco virtual de mediciones DC."""

from src.mediciones import generar_resumen


def mostrar_menu() -> None:
    print("\nBANCO VIRTUAL DE MEDICIONES DC")
    print("1. Registrar medición")
    print("2. Mostrar resumen")
    print("0. Salir")


def ejecutar() -> None:
    """Integra la actividad usando while y match/case."""
    voltajes = []

    # ETAPA 4
    # Debes:
    # 1. Mantener el menú activo con while.
    # 2. Leer una opción.
    # 3. Procesarla con match/case.
    # 4. Opción 1: pedir un voltaje float y agregarlo a `voltajes`.
    # 5. Opción 2: usar generar_resumen(voltajes) y mostrar sus resultados.
    # 6. Opción 0: finalizar.
    # 7. Cualquier otra opción: informar que no es válida.
    pass


if __name__ == "__main__":
    ejecutar()
