import unittest
from Tasks import AdvancedCalc


class TestLike(unittest.TestCase):

    def setUp(self):
        self._test_def = AdvancedCalc.evaluate

    def tearDown(self):
        pass

    def test(self):
        self.assertEqual(self._test_def('5 + (2 - 2 * (3 + 7))'), -13)
        self.assertEqual(self._test_def('6 + pi'), 9.141592653589793)
        self.assertEqual(self._test_def('10 - 3+1'), 8)
        self.assertEqual(self._test_def('10 - 5 * 6'), -20)
        with self.assertRaises(Exception) as context:
            self._test_def('3 * (2 & 1)')
        with self.assertRaises(Exception) as context:
            self._test_def('f(x) = x ** 2 + tg(x)')
        self.assertNotEqual(self._test_def('3 * (2 + 1)'), 10)
        self.assertFalse(self._test_def('10 - 5 * 6') == 30)
        self.assertTrue(type(self._test_def('3 * (2 + 1)')), int)


if __name__ == '__main__':
    unittest.main()