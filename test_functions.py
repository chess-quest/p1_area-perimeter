import unittest
import functions


class TestFormula(unittest.TestCase):
    delta_value = 0.001

    # Tests the function "perimeter_func" when given either whole numbers, floats, or negative numbers
    def test_perim(self):
        self.assertEqual(functions.perimeter_func(1, 3, 0, 0), 12)
        self.assertEqual(functions.perimeter_func(2, 2, 3, 0), 10)
        self.assertAlmostEqual(functions.perimeter_func(3, 5, 0, 0), 31.415, delta=self.delta_value)
        self.assertEqual(functions.perimeter_func(4, 3, 6, 10), 19)

        self.assertAlmostEqual(functions.perimeter_func(1, 5.2, 0, 0), 20.8, delta=self.delta_value)
        self.assertAlmostEqual(functions.perimeter_func(2, 3.42, 1.29, 0), 9.42, delta=self.delta_value)
        self.assertAlmostEqual(functions.perimeter_func(4, 4.67, 1.234, 9.001), 14.905, delta=self.delta_value)

        self.assertEqual(functions.perimeter_func(1, -3 , 0 , 0), -12)
        self.assertEqual(functions.perimeter_func(2, -2, 3, 0), 2)
        self.assertEqual(functions.perimeter_func(2, -2, -3, 0), -10)
        self.assertEqual(functions.perimeter_func(4, -3, -7, 2), -8)

    # Tests the function "area_func" when given either whole numbers, floats, or negative numbers
    def test_area(self):
        self.assertEqual(functions.area_func(1, 3, 0), 9)
        self.assertEqual(functions.area_func(2, 3, 5), 15)
        self.assertAlmostEqual(functions.area_func(3, 5, 0), 78.54, delta=self.delta_value)
        self.assertEqual(functions.area_func(5, 10, 5), 25)

        self.assertAlmostEqual(functions.area_func(1, 1.25, 0), 1.562, delta=self.delta_value)
        self.assertAlmostEqual(functions.area_func(2, 5.551, 8.112), 45.029, delta=self.delta_value)
        self.assertAlmostEqual(functions.area_func(5, 6.123, 0.149), .456, delta=self.delta_value)

        self.assertEqual(functions.area_func(1, -3, 0), 9)
        self.assertEqual(functions.area_func(2, -2, 3), -6)
        self.assertEqual(functions.area_func(2, -2, -3), 6)
        self.assertEqual(functions.area_func(4, -3, -7), 10.5)

