import unittest
from prime_numbers import prime_numbers
from roman_numerals_to_int import roman_numerals_to_int
from text_stat import text_stat

class PrimeNumbersTestCase(unittest.TestCase):   #тесты для проверки работы функции prime_numbers
    def test_PNTest1(self):
        self.assertEqual(prime_numbers('a', True), [])
    def test_PNTest2(self):
        self.assertEqual(prime_numbers('str', 9), [])
    def test_PNTest3(self):
        self.assertEqual(prime_numbers(-5, -7.5), [])
    def test_PNTest4(self):
        self.assertEqual(prime_numbers(-7.0, -5), [])
    def test_PNTest5(self):
        self.assertEqual(prime_numbers(-3.3, 1), [])
    def test_PNTest6(self):
        self.assertEqual(prime_numbers(9, 1.0), [])
    def test_PNTest7(self):
        self.assertEqual(prime_numbers(0, 11.5), [2, 3, 5, 7, 11])
    def test_PNTest8(self):
        self.assertEqual(prime_numbers(-5.5, 11), [2, 3, 5, 7, 11])
    def test_PNTest9(self):
        self.assertEqual(prime_numbers(3, 29.3), [3, 5, 7, 11, 13, 17, 19, 23, 29])

class RNTITestCase(unittest.TestCase):   #тесты для проверки работы функции roman_numerals_to_int
    def test_RNTITest1(self):
        self.assertEqual(roman_numerals_to_int(3), None)
    def test_RNTITest2(self):
        self.assertEqual(roman_numerals_to_int('wow'), None)
    def test_RNTITest3(self):
        self.assertEqual(roman_numerals_to_int('IXA'), None)
    def test_RNTITest4(self):
        self.assertEqual(roman_numerals_to_int('XXXXI'), None)
    def test_RNTITest5(self):
        self.assertEqual(roman_numerals_to_int('XXIX'), 29)
    def test_RNTITest6(self):
        self.assertEqual(roman_numerals_to_int('DXX'), 520)
    def test_RNTITest7(self):
        self.assertEqual(roman_numerals_to_int('CDLXXXI'), 481)

class TSTestCase(unittest.TestCase):   #тесты для проверки работы функции text_stat
    def test_TSTest1(self):
        self.assertEqual(text_stat(20), {'error': 'Аргументом должна быть строка - название файла'})
    def test_TSTest2(self):
        self.assertEqual(text_stat('imagine_file.txt'), {'error': 'Файла с таким именем не существует в данном директории'})
    def test_TSTest3(self):
        self.assertEqual(text_stat('file.txt'), {'A': (0.0, 0.0), 'B': (0.0, 0.0), 'C': (0.0, 0.0), 'D': (0.0, 0.0),
                                                  'E': (0.0, 0.0), 'F': (0.0, 0.0), 'G': (0.0, 0.0), 'H': (0.0, 0.0),
                                                  'I': (0.0, 0.0), 'J': (0.0, 0.0), 'K': (0.01, 0.05),
                                                  'L': (0.01, 0.05), 'M': (0.0, 0.0), 'N': (0.0, 0.0), 'O': (0.0, 0.0),
                                                  'P': (0.0, 0.0), 'Q': (0.0, 0.0), 'R': (0.0, 0.0), 'S': (0.0, 0.0),
                                                  'T': (0.0, 0.0), 'U': (0.0, 0.0), 'V': (0.0, 0.0), 'W': (0.0, 0.0),
                                                  'X': (0.0, 0.0), 'Y': (0.0, 0.0), 'Z': (0.0, 0.0), 'А': (0.13, 0.35),
                                                  'Б': (0.03, 0.15), 'В': (0.04, 0.2), 'Г': (0.02, 0.1),
                                                  'Д': (0.07, 0.35), 'Е': (0.05, 0.25), 'Ё': (0.02, 0.1),
                                                  'Ж': (0.0, 0.0), 'З': (0.0, 0.0), 'И': (0.06, 0.25),
                                                  'Й': (0.01, 0.05), 'К': (0.04, 0.15), 'Л': (0.03, 0.15),
                                                  'М': (0.03, 0.15), 'Н': (0.08, 0.35), 'О': (0.1, 0.35),
                                                  'П': (0.01, 0.05), 'Р': (0.03, 0.1), 'С': (0.06, 0.25),
                                                  'Т': (0.05, 0.2), 'У': (0.03, 0.15), 'Ф': (0.01, 0.05),
                                                  'Х': (0.0, 0.0), 'Ц': (0.01, 0.05), 'Ч': (0.01, 0.05),
                                                  'Ш': (0.0, 0.0), 'Щ': (0.0, 0.0), 'Ъ': (0.0, 0.0), 'Ы': (0.04, 0.2),
                                                  'Ь': (0.0, 0.0), 'Э': (0.0, 0.0), 'Ю': (0.0, 0.0), 'Я': (0.02, 0.1),
                                                  'word_amount': 20, 'paragraph_amount': 3, 'bilingual_amount': 2})

if __name__ == '__main__':
    unittest.main()