import unittest
from Tasks import MoleculeToAtoms


class TestLike(unittest.TestCase):

    def setUp(self):
        self._test_class = MoleculeToAtoms.MyClass()

    def tearDown(self):
        pass

    def test(self):
        self.assertEqual(self._test_class.parse('H2O'), {'H': 2, 'O': 1})
        self.assertEqual(self._test_class.parse('K4[ON(SO3)2]2'), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
        self.assertEqual(self._test_class.parse('6789'), 'Enter the formula of the molecule')
        self.assertNotEqual(self._test_class.parse('Mg(OH)2'), {'Mg': 2, 'O': 2, 'H': 2})
        self.assertTrue(type(self._test_class.parse('Mg(H)2')) == dict)
        self.assertFalse(type(self._test_class.parse('')) == dict)
        self.assertFalse(type(self._test_class.parse('123456')) == dict)


if __name__ == '__main__':
    unittest.main()