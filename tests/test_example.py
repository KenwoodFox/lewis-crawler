import unittest
import lewis_crawler.src.example as example

class TestExample(unittest.TestCase):

    def test_math(self):
        result = example.add(2,4)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()