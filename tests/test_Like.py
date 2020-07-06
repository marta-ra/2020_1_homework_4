import unittest
from Tasks import Like


class TestLike(unittest.TestCase):

    def setUp(self):
        self._test_class = Like.MyClass()

    def tearDown(self):
        pass

    def test(self):
        self.assertEqual(self._test_class.likes(''), 'no one likes this')
        self.assertEqual(self._test_class.likes('"Peter"'), 'Peter likes this')
        self.assertEqual(self._test_class.likes('"Jacob", "Alex"'), 'Jacob and Alex like this')
        self.assertEqual(self._test_class.likes('"Max", "John", "Mark"'), 'Max, John and Mark like this')
        self.assertEqual(self._test_class.likes('"Alex", "Jacob", "Mark", "Max"'), 'Alex, Jacob and 2 others like this')
        self.assertEqual(self._test_class.likes('"Alex", "Jacob", "Mark", "Max", "Anna", "Max", "Kate"'), 'Alex, Jacob and 5 others like this')
        with self.assertRaises(AttributeError):
            num_likes = 5
            self._test_class.likes(num_likes)
        self.assertTrue(type(self._test_class.likes('')) == str)


if __name__ == '__main__':
    unittest.main()
