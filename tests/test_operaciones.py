# tests/test_operaciones.py

import unittest
from operaciones import OperacionesMatematicas

class TestOperacionesMatematicas(unittest.TestCase):

    def test_suma(self):
        resultado = OperacionesMatematicas.suma(5, 3)
        self.assertEqual(resultado, 8)  # Prueba 1: Suma

    def test_resta(self):
        resultado = OperacionesMatematicas.resta(10, 4)
        self.assertEqual(resultado, 6)  # Prueba 2: Resta

    def test_multiplicacion(self):
        resultado = OperacionesMatematicas.multiplicacion(7, 6)
        self.assertEqual(resultado, 42)  # Prueba 3: Multiplicación

    def test_division(self):
        resultado = OperacionesMatematicas.division(20, 5)
        self.assertEqual(resultado, 4)  # Prueba 4: División

    def test_division_por_cero(self):
        with self.assertRaises(ValueError) as contexto:
            OperacionesMatematicas.division(10, 0)
        self.assertEqual(str(contexto.exception), "Error: División por cero")  # Prueba 5: División por cero

if __name__ == '__main__':
    unittest.main()
