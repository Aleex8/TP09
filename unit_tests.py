import unittest
from fraction import Fraction

class FractionTestCase(unittest.TestCase):

    def test_init(self):
        Fraction_1 = Fraction(1, 2)
        self.assertEqual(Fraction_1.numerator, 1)
        self.assertEqual(Fraction_1.denominator, 2)

        Fraction_2 = Fraction(0, 1)
        self.assertEqual(Fraction_2.numerator, 0)
        self.assertEqual(Fraction_2.denominator, 1)

        Fraction_3 = Fraction(4, 8)
        self.assertEqual(Fraction_3.numerator, 1)
        self.assertEqual(Fraction_3.denominator, 2)

        Fraction_4 = Fraction(-1, 2)
        self.assertEqual(Fraction_4.numerator, -1)
        self.assertEqual(Fraction_4.denominator, 2)

        Fraction_5 = Fraction(1, -2)
        self.assertEqual(Fraction_5.numerator, -1)
        self.assertEqual(Fraction_5.denominator, 2)

        Fraction_6 = Fraction(-1, -2)
        self.assertEqual(Fraction_6.numerator, 1)
        self.assertEqual(Fraction_6.denominator, 2)

        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)

        self.assertRaises(TypeError, Fraction, "un", 2)

    def test_str(self):
        Fraction_7 = Fraction(1, 1)
        self.assertEqual(str(Fraction_7), "1/1")

        Fraction_8 = Fraction(0, 1)
        self.assertEqual(str(Fraction_8), "0/1")

        Fraction_9 = Fraction(10, 40)
        self.assertEqual(str(Fraction_9), "1/4")

        Fraction_10 = Fraction(-1, 2)
        self.assertEqual(str(Fraction_10), "-1/2")

        Fraction_11 = Fraction(1, -2)
        self.assertEqual(str(Fraction_11), "-1/2")

        Fraction_12 = Fraction(-1, -2)
        self.assertEqual(str(Fraction_12), "1/2")

    def test_add(self):
        Fraction_13 = Fraction(4, 1)
        Fraction_14 = Fraction(4, 2)
        self.assertEqual(Fraction_13 + Fraction_14,6)

        Fraction_15 = Fraction(1, 2)
        Fraction_16 = Fraction(3, 4)
        self.assertEqual(Fraction_15 + Fraction_16, 5/4)

        Fraction_17 = Fraction(1, 2)
        Fraction_18 = Fraction(-3, 4)
        self.assertEqual(Fraction_17 + Fraction_18, -1/4)

        Fraction_19 = Fraction(1, 2)
        Fraction_20 = Fraction(-1, 2)
        self.assertEqual(Fraction_19 + Fraction_20,0)

        Fraction_21 = Fraction(-1, 2)
        Fraction_22 = Fraction(-1, 2)
        self.assertEqual(Fraction_21 + Fraction_22, -1)

    def test_sub(self):
        Fraction_23 = Fraction(4, 2)
        Fraction_24 = Fraction(1, 1)
        self.assertEqual(Fraction_23 - Fraction_24, 1)

        Fraction_25 = Fraction(3, 4)
        Fraction_26 = Fraction(1, 2)
        self.assertEqual(Fraction_25 - Fraction_26, 1/4)

        Fraction_27 = Fraction(1, 2)
        Fraction_28 = Fraction(-1, 2)
        self.assertEqual(Fraction_27 - Fraction_28, 1)

        Fraction_29 = Fraction(1, 2)
        Fraction_30 = Fraction(1, 2)
        self.assertEqual(Fraction_29 - Fraction_30, 0)

        Fraction_31 = Fraction(-1, 2)
        Fraction_32 = Fraction(1, 2)
        self.assertEqual(Fraction_31 - Fraction_32, -1)

    def test_mul(self):
        Fraction_33 = Fraction(2, 1)
        Fraction_34 = Fraction(2, 2)
        self.assertEqual(Fraction_33 * Fraction_34, 2)

        Fraction_35 = Fraction(1, 2)
        Fraction_36 = Fraction(3, 4)
        self.assertEqual(Fraction_35 * Fraction_36, 3/8)

        Fraction_37 = Fraction(-1, 2)
        Fraction_38 = Fraction(1, 2)
        self.assertEqual(Fraction_37 * Fraction_38, -1/4)

        Fraction_39 = Fraction(0, 1)
        Fraction_40 = Fraction(1, 2)
        self.assertEqual(Fraction_39 * Fraction_40,0)

    def test_truediv(self):
        Fraction_41 = Fraction(8, 1)
        Fraction_42 = Fraction(4, 2)
        self.assertEqual(Fraction_41 / Fraction_42, 4)

        Fraction_43 = Fraction(2, 5)
        Fraction_44 = Fraction(1, 2)
        self.assertEqual(Fraction_43 / Fraction_44, 4/5)

        Fraction_45 = Fraction(-2, 5)
        Fraction_46 = Fraction(1, 2)
        self.assertEqual(Fraction_45 / Fraction_46, -4/5)

        Fraction_45 = Fraction(0, 5)
        Fraction_46 = Fraction(1, 2)
        self.assertEqual(Fraction_45 / Fraction_46,0)

        with self.assertRaises(ZeroDivisionError):
            Fraction_47 = Fraction(1, 2)
            Fraction_48 = Fraction(0, 1)
            return Fraction_47/Fraction_48

    def test_eq(self):
        Fraction_49 = Fraction(5, 5)
        Fraction_50 = Fraction(1, 1)
        self.assertTrue(Fraction_49 == Fraction_50)

        Fraction_51 = Fraction(2, 5)
        Fraction_52 = Fraction(1, 2)
        self.assertFalse(Fraction_51 == Fraction_52)

    def test_is_integer(self):
        Fraction_53 = Fraction(8, 4)
        self.assertTrue(Fraction_53.is_integer())

        Fraction_54 = Fraction(1, 4)
        self.assertFalse(Fraction_54.is_integer())

    def test_is_proper(self):
        Fraction_55 = Fraction(1, 4)
        self.assertTrue(Fraction_55.is_proper())

        Fraction_56 = Fraction(-1, 4)
        self.assertTrue(Fraction_56.is_proper())

        Fraction_57 = Fraction(8, 4)
        self.assertFalse(Fraction_57.is_proper())

        Fraction_58 = Fraction(-8, 4)
        self.assertFalse(Fraction_58.is_proper())

    def test_is_zero(self):
        Fraction_59 = Fraction(0, 1)
        self.assertTrue(Fraction_59.is_zero())

    def test_is_unit(self):
        Fraction_60 = Fraction(1, 2)
        self.assertTrue(Fraction_60.is_unit())





if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

