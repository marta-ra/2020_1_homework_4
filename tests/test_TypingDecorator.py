import unittest
from Tasks import TypingDecorator


class TestLike(unittest.TestCase):

    def setUp(self):
        self._test_def_add = TypingDecorator.MyClass.add
        self._test_def_convert_upper = TypingDecorator.MyClass.convert_upper
        self._test_def_acc = TypingDecorator.MyClass.acc


    def tearDown(self):
        pass

    def test(self):
        self.assertEqual(self._test_def_add(self, 4, True), '5')
        self.assertEqual(self._test_def_add(self, 2, 5), '7')
        self.assertEqual(self._test_def_add(self, '6', '4'), '10')
        self.assertNotEqual(self._test_def_add(self, 13, False), 14)
        self.assertTrue(type(self._test_def_add(self, 1, 4)), int)
        self.assertEqual(self._test_def_convert_upper(self, 'j'), 'J')
        self.assertTrue(type(self._test_def_convert_upper(self, 'k')), str)
        with self.assertRaises(TypeError):
            a = 5
            self._test_def_convert_upper(a)
        self.assertEqual(self._test_def_acc(self, 'a', 'b', 'c'), 'abc')
        self.assertEqual(self._test_def_acc(self, 0.1, 0.2, 0.4), 0.7000000000000001)
        self.assertTrue(type(self._test_def_acc(self, 0.1, 0.2, 0.4)), float)
        self.assertFalse(type(self._test_def_acc(self, 'a', 'f', 'g')) == int)





if __name__ == '__main__':
    unittest.main()