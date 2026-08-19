import ast
import inspect
import unittest

from src.mediciones import calcular_promedio, contar_fuera_rango, buscar_primero_normal


class TestEtapa3(unittest.TestCase):
    def test_calcular_promedio(self):
        self.assertAlmostEqual(calcular_promedio([5.0, 4.5, 5.1, 5.4]), 5.0)
        self.assertEqual(calcular_promedio([]), 0.0)

    def test_promedio_usa_for(self):
        arbol = ast.parse(inspect.getsource(calcular_promedio))
        self.assertTrue(any(isinstance(nodo, ast.For) for nodo in ast.walk(arbol)))

    def test_contar_fuera_rango(self):
        self.assertEqual(contar_fuera_rango([5.0, 4.5, 5.1, 5.4]), 2)
        self.assertEqual(contar_fuera_rango([4.75, 5.0, 5.25]), 0)

    def test_contar_usa_for(self):
        arbol = ast.parse(inspect.getsource(contar_fuera_rango))
        self.assertTrue(any(isinstance(nodo, ast.For) for nodo in ast.walk(arbol)))

    def test_buscar_primero_normal(self):
        self.assertEqual(buscar_primero_normal([4.0, 4.6, 5.1, 5.3]), 5.1)
        self.assertIsNone(buscar_primero_normal([4.0, 4.6, 5.3]))

    def test_busqueda_usa_while(self):
        arbol = ast.parse(inspect.getsource(buscar_primero_normal))
        self.assertTrue(any(isinstance(nodo, ast.While) for nodo in ast.walk(arbol)))


if __name__ == "__main__":
    unittest.main()
