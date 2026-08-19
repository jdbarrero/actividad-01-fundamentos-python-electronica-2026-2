import unittest

from src.mediciones import crear_medicion, calcular_potencia


class TestEtapa1(unittest.TestCase):
    def test_crear_medicion_conserva_datos_y_orden(self):
        medicion = crear_medicion(1, "TP1", 5.02, 0.20, True, 10 + 2j)
        self.assertEqual(medicion, [1, "TP1", 5.02, 0.20, True, 10 + 2j])

    def test_crear_medicion_conserva_tipos(self):
        medicion = crear_medicion(2, "TP2", 4.98, 0.15, False, 3 + 4j)
        self.assertIsInstance(medicion[0], int)
        self.assertIsInstance(medicion[1], str)
        self.assertIsInstance(medicion[2], float)
        self.assertIsInstance(medicion[3], float)
        self.assertIsInstance(medicion[4], bool)
        self.assertIsInstance(medicion[5], complex)

    def test_calcular_potencia(self):
        self.assertAlmostEqual(calcular_potencia(5.0, 0.2), 1.0)
        self.assertAlmostEqual(calcular_potencia(12.0, 0.5), 6.0)


if __name__ == "__main__":
    unittest.main()
