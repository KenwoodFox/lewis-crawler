import unittest, os
import lewis_crawler.src.sstv as sstv


class TestExample(unittest.TestCase):

    def test_math(self):
        sstv.do_test() # Do the test
        assert os.path.exists('lewis_crawler\working\working.wav')


if __name__ == '__main__':
    unittest.main()
