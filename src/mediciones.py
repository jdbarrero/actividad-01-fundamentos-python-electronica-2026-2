"""Funciones del banco virtual de mediciones DC."""

from src.config import LIMITE_INFERIOR, LIMITE_SUPERIOR


def crear_medicion(
    numero: int,
    punto: str,
    voltaje: float,
    corriente: float,
    activo: bool,
    impedancia: complex,
) -> list:
    """Retorna los seis datos recibidos dentro de una lista, en el mismo orden."""
    # ETAPA 1
    pass


def calcular_potencia(voltaje: float, corriente: float) -> float:
    """Calcula la potencia eléctrica P = V * I."""
    # ETAPA 1
    pass


def clasificar_voltaje(voltaje: float) -> str:
    """Retorna BAJO, NORMAL o ALTO usando if / elif / else."""
    # ETAPA 2
    pass


def calcular_promedio(voltajes: list) -> float:
    """Calcula el promedio recorriendo la lista con for. Lista vacía -> 0.0."""
    # ETAPA 3
    pass


def contar_fuera_rango(voltajes: list) -> int:
    """Cuenta con for cuántos voltajes están fuera del rango normal."""
    # ETAPA 3
    pass


def buscar_primero_normal(voltajes: list):
    """Busca con while el primer voltaje NORMAL. Si no existe, retorna None."""
    # ETAPA 3
    pass


def generar_resumen(voltajes: list) -> list:
    """Retorna [promedio, cantidad_fuera_rango, primer_voltaje_normal]."""
    # ETAPA 4
    pass
