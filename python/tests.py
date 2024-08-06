import unittest

from functions import eval_exp


class TestEvalExp(unittest.TestCase):
    def test_0(self):
        exp = "1 + 3"
        result = eval_exp(exp)
        expected = '4'
        self.assertEqual(result, expected)

    def test_1(self):
        exp = "1 + 2 * 3"
        result = eval_exp(exp)
        expected = '7'
        self.assertEqual(result, expected)

    def test_2(self):
        exp = "4 / 2 + 7"
        result = eval_exp(exp)
        expected = '9'
        self.assertEqual(result, expected)

    def test_3(self):
        exp = "1 + 2 + 3 * 4"
        result = eval_exp(exp)
        expected = '15'
        self.assertEqual(result, expected)

    def test_4(self):
        exp = "(1 + 2 + 3) * 4"
        result = eval_exp(exp)
        expected = '24'
        self.assertEqual(result, expected)

    def test_5(self):
        exp = "(10 / 3 + 23) * (1 - 4)"
        result = eval_exp(exp)
        expected = '-78'
        self.assertEqual(result, expected)

    def test_6(self):
        exp = "((1 + 3) * 8 + 1) / 3"
        result = eval_exp(exp)
        expected = '11'
        self.assertEqual(result, expected)

    def test_7(self):
        exp = "58 - -8 * (58 + 31) - -14"
        result = eval_exp(exp)
        expected = '784'
        self.assertEqual(result, expected)

    def test_8(self):
        exp = "-71 * (-76 * 91 * (10 - 5 - -82) - -79)"
        result = eval_exp(exp)
        expected = '42714523'
        self.assertEqual(result, expected)

    def test_9(self):
        exp = "10 * 20 + 3 * 7 + 2 * 3 + 10 / 3 * 4"
        result = eval_exp(exp)
        expected = '239'
        self.assertEqual(result, expected)

    def test_10(self):
        exp = "(-13 - -73) * (44 - -78 - 77 + 42 - -32)"
        result = eval_exp(exp)
        expected = '7140'
        self.assertEqual(result, expected)

    def test_11(self):
        exp = "-29 * 49 + 47 - 29 + 74 - -85 - -27 + 4 - 28"
        result = eval_exp(exp)
        expected = '-1241'
        self.assertEqual(result, expected)

    def test_12(self):
        exp = "-74 - -14 + 42 - -4 + -78 + -50 * -35 * -81 + -41"
        result = eval_exp(exp)
        expected = '-141883'
        self.assertEqual(result, expected)

    def test_13(self):
        exp = "80 * -18 * (85 * (-46 + -71) - 12 + 26 - 59) + 84"
        result = eval_exp(exp)
        expected = '14385684'
        self.assertEqual(result, expected)

    def test_14(self):
        exp = "25 + 38 + 88 + (-6 - -73) * (-83 + (53 + 97) * 14)"
        result = eval_exp(exp)
        expected = '135290'
        self.assertEqual(result, expected)

    def test_15(self):
        exp = "(84 - 90) * (-8 - 75 + -83 * (56 - -77) + 4 + -94)"
        result = eval_exp(exp)
        expected = '67272'
        self.assertEqual(result, expected)

    def test_16(self):
        exp = "(54 - -8 - -35 + -68 - -90) * -39 + -43 + -91 * -30"
        result = eval_exp(exp)
        expected = '-1954'
        self.assertEqual(result, expected)

    def test_17(self):
        exp = "-13 - -74 + (66 + -57) * -93 * -9 * 77 + 79 - 66 + -53"
        result = eval_exp(exp)
        expected = '580062'
        self.assertEqual(result, expected)

    def test_18(self):
        exp = "(-72 - 50 * -74 + -45) * 92 * 21 * 5 * (-13 - 66 - 18)"
        result = eval_exp(exp)
        expected = '-3357342660'
        self.assertEqual(result, expected)

    def test_19(self):
        exp = "-7 - -37 * (90 + 70) - 30 - -44 + -32 - 56 - -48 - -78"
        result = eval_exp(exp)
        expected = '5965'
        self.assertEqual(result, expected)

    def test_20(self):
        exp = "65 * -83 - -3 + -20 + 24 - 85 * (-24 + -32) * (61 - 20)"
        result = eval_exp(exp)
        expected = '189772'
        self.assertEqual(result, expected)

    def test_21(self):
        exp = "55 * 48 * -44 - -32 + 1 * -80 * -94 - 74 * -53 + -30 + -61"
        result = eval_exp(exp)
        expected = '-104777'
        self.assertEqual(result, expected)

    def test_22(self):
        exp = "-82 * (25 + 62 + 3) - -72 + -65 * -32 * (77 + 12) - -95 + 51"
        result = eval_exp(exp)
        expected = '177958'
        self.assertEqual(result, expected)

    def test_23(self):
        exp = "(2 - 65 - (-24 + -97) * -5 * -61) * (-41 + 85 * 9 * -92 * (75 - 18))"
        result = eval_exp(exp)
        expected = '-147799088242'
        self.assertEqual(result, expected)

    def test_24(self):
        exp = "-20 + -51 + 20 + -68 * -11 + -35 * -14 - 95 - 32 + -52 * -23 - -90 * -42"
        result = eval_exp(exp)
        expected = '-1524'
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
