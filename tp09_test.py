import unittest
from tp07vbrichant import Fraction


class FractionTestCase(unittest.TestCase):
    """
    Contains all test for Fraction
    """
    def tests_raises(self):
        """Tests for the exceptions that should be raised """
        self.assertRaises(ZeroDivisionError, Fraction, 5, 0)
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "str"
        with self.assertRaises(TypeError):
            Fraction(1, 2) - "str"
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "str"
        with self.assertRaises(TypeError):
            Fraction(1, 2) / "str"
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 3)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0)
        with self.assertRaises(TypeError):
            Fraction(1, 2) == "str"
        with self.assertRaises(TypeError):
            Fraction(1, 2) ** "str"

    def tests_init(self):
        """Tests for the init of Fraction"""
        init_test = Fraction(5, 4)
        self.assertEqual(init_test.numerator, 5)
        self.assertEqual(init_test.denominator, 4)
        init_test2 = Fraction(-1, 2)
        self.assertEqual(init_test2.numerator, -1)
        self.assertEqual(init_test2.denominator, 2)
        init_test3 = Fraction(0, 2)
        self.assertEqual(init_test3.numerator, 0)
        self.assertEqual(init_test3.denominator, 2)

    def tests_str(self):
        """Tests for the str method"""
        self.assertEqual(str(Fraction(5, 4)), "5 / 4")
        self.assertEqual(str(Fraction(25, 3)), "25 / 3")
        self.assertEqual(str(Fraction(-2, 3)), "-2 / 3")
        self.assertEqual(str(Fraction(1)), "1 / 1")
        self.assertEqual(str(Fraction(-1)), "-1 / 1")
        self.assertEqual(str(Fraction(0)), "0 / 1")

    def tests_mixed_number(self):
        """Tests for the mixed numbers method"""
        self.assertEqual(Fraction(1).as_mixed_number(), "1")
        self.assertEqual(Fraction(-1).as_mixed_number(), "-1")
        self.assertEqual(Fraction(-2).as_mixed_number(), "-2")
        self.assertEqual(Fraction(-1, 2).as_mixed_number(), "-1 / 2")
        self.assertEqual(Fraction(0).as_mixed_number(), "0")
        self.assertEqual(Fraction(25, 5).as_mixed_number(), "5")
        self.assertEqual(Fraction(-16, 4).as_mixed_number(), "-4")
        self.assertEqual(Fraction(3, 4).as_mixed_number(), "3 / 4")
        self.assertEqual(Fraction(6, 8).as_mixed_number(), "3 / 4")
        self.assertEqual(Fraction(9, 4).as_mixed_number(), "2 + 1 / 4")
        self.assertEqual(Fraction(-7, 2).as_mixed_number(), "-3 + 1 / 2")
        self.assertEqual(Fraction(-5, 3).as_mixed_number(), "-1 + 2 / 3")

    def tests_operators_add(self):
        """Tests for '+' operator"""
        self.assertEqual(Fraction(1, 2) + Fraction(3, 4), Fraction(5, 4))
        self.assertEqual(Fraction(3, 4) + Fraction(8, 24), Fraction(26, 24))
        self.assertEqual(Fraction(1, 2) + Fraction(8, 24), Fraction(20, 24))
        self.assertEqual(Fraction(1, 2) + Fraction(0, 24), Fraction(1, 2))
        self.assertEqual(Fraction(-2, 5) + Fraction(2, 3), Fraction(4, 15))
        self.assertEqual(Fraction(1, 1) + 1, Fraction(2, 1))
        self.assertEqual(Fraction(1, 1) + 0, Fraction(1, 1))
        self.assertEqual(Fraction(1, 1) + -1, Fraction(0, 1))

    def tests_operators_sub(self):
        """Tests for '-' operator"""
        self.assertEqual(Fraction(1, 2) - Fraction(3, 4), Fraction(-1, 4))
        self.assertEqual(Fraction(3, 4) - Fraction(8, 24), Fraction(10, 24))
        self.assertEqual(Fraction(1, 2) - Fraction(8, 24), Fraction(4, 24))
        self.assertEqual(Fraction(-3, 7) - Fraction(5, 4), Fraction(-47, 28))
        self.assertEqual(Fraction(1, 1) - 1, Fraction(0, 1))
        self.assertEqual(Fraction(1, 1) - 0, 1)
        self.assertEqual(Fraction(4, 7) - 0, Fraction(4, 7))
        self.assertEqual(Fraction(4, 7) - Fraction(0, 7), Fraction(4, 7))
        self.assertEqual(Fraction(1, 1) - -1, Fraction(2, 1))

    def tests_operators_mul(self):
        """Tests for '*' operator"""
        self.assertEqual(Fraction(1, 2) * Fraction(3, 4), Fraction(3, 8))
        self.assertEqual(Fraction(3, 4) * Fraction(8, 24), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) * Fraction(8, 24), Fraction(1, 6))
        self.assertEqual(Fraction(1, 2) * Fraction(0, 3), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) * Fraction(0), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) * Fraction(0), Fraction(0))
        self.assertEqual(Fraction(-3, 7) * Fraction(5, 4), Fraction(-15, 28))
        self.assertEqual(Fraction(-3, 7) * 1, Fraction(-3, 7))
        self.assertEqual(Fraction(-3, 7) * -1, Fraction(3, 7))
        self.assertEqual(Fraction(-3, 7) * 0, Fraction(0, 1))

    def tests_operators_div(self):
        """Tests for '/' operator"""
        self.assertEqual(Fraction(1, 2) / Fraction(3, 4), Fraction(2, 3))
        self.assertEqual(Fraction(3, 4) / Fraction(8, 24), Fraction(9, 4))
        self.assertEqual(Fraction(1, 2) / Fraction(8, 24), Fraction(3, 2))
        self.assertEqual(Fraction(-3, 7) / Fraction(5, 4), Fraction(-12, 35))
        self.assertEqual(Fraction(-3, 7) / 1, Fraction(-3, 7))
        self.assertEqual(Fraction(-3, 7) / -1, Fraction(3, 7))
        self.assertEqual(Fraction(3, 7) / -1, Fraction(-3, 7))

    def tests_operators_eq(self):
        """Tests for '==' operator"""
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))
        self.assertFalse(Fraction(3, 4) == Fraction(8, 24))
        self.assertFalse(Fraction(1, 2) == Fraction(8, 24))
        self.assertTrue(Fraction(3, 4) == Fraction(3, 4))
        self.assertTrue(Fraction(8, 24) == Fraction(8, 24))
        self.assertTrue(Fraction(-12, 7) == Fraction(-24, 14))
        self.assertTrue(Fraction(7, 7) == 1)
        self.assertTrue(Fraction(-12, 12) == -1)
        self.assertTrue(Fraction(0, 7) == 0)

    def tests_operators_pow(self):
        """Tests for '**' operator"""
        self.assertEqual(Fraction(1, 2) ** 2, Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) ** 3, Fraction(1, 8))
        self.assertEqual(Fraction(1, 2) ** 4, Fraction(1, 16))
        self.assertEqual(Fraction(-2, 3) ** 6, Fraction(64, 729))
        self.assertEqual(Fraction(1, 2) ** 1, Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) ** 0, Fraction(1, 1))

    def tests_is_zero(self):
        """Tests for is_zero function"""
        self.assertFalse(Fraction(1, 2).is_zero())
        self.assertFalse(Fraction(3, 1).is_zero())
        self.assertFalse(Fraction(-3, 1).is_zero())
        self.assertTrue(Fraction(0, 12).is_zero())

    def tests_is_interger(self):
        """Tests for is_integer function"""
        self.assertFalse(Fraction(1, 2).is_integer())
        self.assertFalse(Fraction(14, 3).is_integer())
        self.assertTrue(Fraction(24, 12).is_integer())
        self.assertTrue(Fraction(3, 1).is_integer())

    def tests_is_proper(self):
        """Tests for is_proper function"""
        self.assertFalse(Fraction(3, 2).is_proper())
        self.assertFalse(Fraction(14, 3).is_proper())
        self.assertTrue(Fraction(7, 12).is_proper())
        self.assertTrue(Fraction(-1, 2).is_proper())

    def tests_is_unit(self):
        """Tests for is_unit function"""
        self.assertFalse(Fraction(5, 3).is_unit())
        self.assertFalse(Fraction(14, 3).is_unit())
        self.assertTrue(Fraction(1, 12).is_unit())
        self.assertTrue(Fraction(2, 12).is_unit())

    def tests_is_adjacent_to(self):
        """Tests for is_adjacent_to function"""
        self.assertFalse(Fraction(5, 3).is_adjacent_to(Fraction(4, 8)))
        self.assertFalse(Fraction(14, 3).is_adjacent_to(Fraction(7, 8)))
        self.assertTrue(Fraction(1, 3).is_adjacent_to(Fraction(1, 4)))
        self.assertTrue(Fraction(1, 4).is_adjacent_to(Fraction(1, 3)))


if __name__ == "__main__":
    unittest.main()
