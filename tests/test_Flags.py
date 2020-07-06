import unittest
from Tasks import Flags


class TestLike(unittest.TestCase):

    def setUp(self):
        self._test_def = Flags.MyClass()

    def tearDown(self):
        pass

    def test(self):
        self.assertEqual(self._test_def.flags(4), '|1 / |2 / |3 / |4 / ')
        self.assertNotEqual(self._test_def.flags(4), '|1/ |2/ |3/ |4/ ')
        self.assertNotEqual(self._test_def.flags(4), '|1 / |2 / |3 / ')
        self.assertEqual(self._test_def.flags(10), 'Enter value greater than 0 and less than 10')
        self.assertEqual(self._test_def.flags(0), 'Enter value greater than 0 and less than 10')
        self.assertEqual(self._test_def.lst(3), [1, 2, 3])
        self.assertIs(len(self._test_def.lst(9)), 9)


if __name__ == '__main__':
    unittest.main()