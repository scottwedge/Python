def promedio(valores):
    """Calcula la media aritmetica de una lista de numeros.

    >>> print promedio([20, 30, 70])
    40.0
    """
    return sum(valores, 0.0) / len(valores)

import doctest
doctest.testmod() # Valida automaticamente las pruebas integradas

import unittest
class TestFuncionesEstadisticas(unittest.TestCase):

	def test_promedio(self):
		self.assertEqual(promedio([20, 30, 70]), 40.0)
		self.assertEqual(round(promedio([1, 5, 7]), 1), 4.3)
		self.assertRaises(ZeroDivisionError, promedio, [])
		self.assertRaises(TypeError, promedio, 20, 30, 70)

unnitest.main()
