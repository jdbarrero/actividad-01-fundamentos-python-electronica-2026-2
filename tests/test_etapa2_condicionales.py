import ast
import inspect
import unittest

from src.mediciones import clasificar_voltaje


class TestEtapa2(unittest.TestCase):
    def test_clasificaciones(self):
        self.assertEqual(clasificar_voltaje(4.50), "BAJO")
        self.assertEqual(clasificar_voltaje(5.00), "NORMAL")
        self.assertEqual(clasificar_voltaje(5.40), "ALTO")

    def test_limites_son_normales(self):
        self.assertEqual(clasificar_voltaje(4.75), "NORMAL")
        self.assertEqual(clasificar_voltaje(5.25), "NORMAL")

    def test_usa_condicional(self):
        arbol = ast.parse(inspect.getsource(clasificar_voltaje))
        self.assertTrue(any(isinstance(nodo, ast.If) for nodo in ast.walk(arbol)))


if __name__ == "__main__":
    unittest.main()
