# -*- coding: utf-8 -*-

import unittest

from calculator import Calculator, CalculatorSyntaxError


class TestsCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        self.calculator = None

    # ------------ Tests -------------

    def test_add_1_plus_2(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_1_plus_5(self):
        result = self.calculator.add(1, 5)
        self.assertEqual(result, 6)

    def test_commutative_property(self):
        resultA = self.calculator.add(1, 5)
        resultB = self.calculator.add(5, 1)
        self.assertEqual(resultA, resultB)

    def test_subtract_1_minus_6(self):
        result = self.calculator.subtract(1, 6)
        self.assertEqual(result, -5)

    def test_subtract_5_minus_6(self):
        result = self.calculator.subtract(5, 6)
        self.assertEqual(result, -1)

    def test_subtract_non_commutative_property(self):
        resultA = self.calculator.subtract(1,6)
        resultB = self.calculator.subtract(6,1)
        self.assertNotEqual(resultA, resultB)

    def test_eval_add_4_6(self):
        result = self.calculator.eval("4 + 6")
        self.assertEqual(result, 10)

    def test_eval_add_4_6(self):
        result = self.calculator.eval("6 + 6")
        self.assertEqual(result, 12)

    def test_parse_add_4_6(self):
        result = self.calculator.parse("4 + 6")
        self.assertEqual(result, [4, "+", 6])

    def test_parse_add_6_6(self):
        result = self.calculator.parse("6 + 6")
        self.assertEqual(result, [6, "+", 6])

    def test_parse_add_1_2_3(self):
        result = self.calculator.parse("1 + 2 + 3")
        self.assertEqual(result, [1, "+", 2, "+", 3])

    def test_parse_subtract_1_6(self):
        result = self.calculator.parse("1 - 6")
        self.assertEqual(result, [1, "-", 6])

    def test_bad_expression_syntax_with_two_operators(self):
        with self.assertRaises(CalculatorSyntaxError):
            result = self.calculator.parse("1 + + 3")

    def test_bad_expression_syntax_with_unknown_item_raises_exception(self):
        with self.assertRaises(CalculatorSyntaxError):
            result = self.calculator.parse("1 + casa")

    def test_bad_expression_syntax_with_two_numbers_without_operator_between(self):
        with self.assertRaises(CalculatorSyntaxError):
            result = self.calculator.parse("1 + 2 3")

# comprueba si se está ejecutando directamente este archivo con el comando: python tests.py y, de ser así, arranca los tests py
if __name__ == "__main__":
    unittest.main()

