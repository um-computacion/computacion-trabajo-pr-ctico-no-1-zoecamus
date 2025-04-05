import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    #1
    def test_numero_romano1(self):
        self.assertEqual(decimal_to_roman(1), "I")
    #2
    def test_numero_romano2(self):
        self.assertEqual(decimal_to_roman(2), "II")
    #3
    def test_numero_romano3(self):
        self.assertEqual(decimal_to_roman(3), "III")
    #4
    def test_numero_romano4(self):
        self.assertEqual(decimal_to_roman(4), "IV")
    #5
    def test_numero_romano5(self):
        self.assertEqual(decimal_to_roman(5), "V")
    #6
    def test_numero_romano6(self):
        self.assertEqual(decimal_to_roman(6), "VI")
    #7
    def test_numero_romano7(self):
        self.assertEqual(decimal_to_roman(7), "VII")
    #8
    def test_numero_romano8(self):
        self.assertEqual(decimal_to_roman(8), "VIII")
    #9
    def test_numero_romano9(self):
        self.assertEqual(decimal_to_roman(9), "IX")
    #10
    def test_numero_romano10(self):
        self.assertEqual(decimal_to_roman(10), "X")
    #11
    def test_numero_romano11(self):
        self.assertEqual(decimal_to_roman(11), "XI")
    #40
    def test_numero_romano40(self):
        self.assertEqual(decimal_to_roman(40), "XL")
    #49
    def test_numero_romano49(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
    #50
    def test_numero_romano50(self):
        self.assertEqual(decimal_to_roman(50), "L")
    #100
    def test_numero_romano100(self):
        self.assertEqual(decimal_to_roman(100), "C")
    #500
    def test_numero_romano500(self):
        self.assertEqual(decimal_to_roman(500), "D")
    #999
    def test_numero_romano999(self):
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
    #1000
    def test_numero_romano1000(self):
        self.assertEqual(decimal_to_roman(1000), "M")
    #3000
    def test_numero_romano3000(self):
        self.assertEqual(decimal_to_roman(3000), "MMM")
    #3999
    def test_numero_romano3999(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()
 