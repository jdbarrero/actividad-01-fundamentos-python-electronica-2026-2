import ast
import inspect
import unittest

from src.app import ejecutar
from src.mediciones import generar_resumen


class TestEtapa4(unittest.TestCase):
    def test_generar_resumen(self):
        resumen = generar_resumen([4.0, 5.0, 5.1])
        self.assertAlmostEqual(resumen[0], 4.7)
        self.assertEqual(resumen[1], 1)
        self.assertEqual(resumen[2], 5.0)

    def test_resumen_vacio(self):
        self.assertEqual(generar_resumen([]), [0.0, 0, None])

    def test_app_usa_while(self):
        arbol = ast.parse(inspect.getsource(ejecutar))
        self.assertTrue(any(isinstance(nodo, ast.While) for nodo in ast.walk(arbol)))

    def test_app_usa_match(self):
        arbol = ast.parse(inspect.getsource(ejecutar))
        self.assertTrue(any(isinstance(nodo, ast.Match) for nodo in ast.walk(arbol)))


if __name__ == "__main__":
    unittest.main()
