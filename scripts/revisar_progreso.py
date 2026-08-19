"""Verificador progresivo y amigable para estudiantes.

Revisa una etapa a la vez y se detiene en la primera que todavía falla.
No muestra trazas extensas: únicamente los nombres de las pruebas pendientes.
"""

from pathlib import Path
import sys
import unittest


ETAPAS = [
    ("Etapa 1 — Tipos de datos y operadores", "tests.test_etapa1_tipos_operadores"),
    ("Etapa 2 — Condicionales", "tests.test_etapa2_condicionales"),
    ("Etapa 3 — Listas y ciclos", "tests.test_etapa3_listas_ciclos"),
    ("Etapa 4 — Funciones e integración", "tests.test_etapa4_integracion"),
]


class ResultadoSilencioso(unittest.TestResult):
    """Resultado estándar de unittest sin imprimir trazas extensas."""


def nombre_prueba(test: unittest.case.TestCase) -> str:
    return test.id().split(".")[-1]


def ejecutar_etapa(nombre: str, modulo: str) -> bool:
    print("\n" + "=" * 64)
    print(nombre)
    print("=" * 64)

    suite = unittest.defaultTestLoader.loadTestsFromName(modulo)
    resultado = ResultadoSilencioso()
    suite.run(resultado)

    total = resultado.testsRun
    pendientes = [test for test, _ in resultado.failures] + [test for test, _ in resultado.errors]

    if resultado.wasSuccessful():
        print(f"✅ {total} pruebas superadas.")
        return True

    print(f"❌ {len(pendientes)} de {total} pruebas todavía necesitan trabajo.")
    print("\nRevisa estos comportamientos:")
    for test in pendientes:
        print(f"  - {nombre_prueba(test)}")

    return False


def main() -> int:
    raiz = Path(__file__).resolve().parents[1]
    if Path.cwd().resolve() != raiz:
        print("Ejecuta este comando desde la raíz del repositorio:")
        print("python scripts/revisar_progreso.py")
        return 2

    if str(raiz) not in sys.path:
        sys.path.insert(0, str(raiz))

    print("\nBANCO VIRTUAL DE MEDICIONES DC")
    print("Revisión progresiva del aprendizaje")

    for nombre, modulo in ETAPAS:
        if ejecutar_etapa(nombre, modulo):
            continue

        print(f"\n👉 Esta es la primera etapa que debes trabajar: {nombre}")
        print("Corrige únicamente esta etapa y vuelve a ejecutar:")
        print("python scripts/revisar_progreso.py")
        return 1

    print("\n🎉 Todas las etapas fueron superadas.")
    print("Ahora ejecuta: python -m src.app")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
