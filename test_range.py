import unittest
from RangeGenerator import RangeGenerator
class TestRange(unittest.TestCase):
    def setUp(self):
        self.range_generator = RangeGenerator()

    def assert_range_generator(self, range, set_expected):
        set_result = self.range_generator.generate(range)
        self.assertEqual(set_expected, set_result)

    def test_range_open_zero_zero_open(self):
        self.assert_range_generator("(0,0)","{}")
    
    def test_range_open_one_one_open(self):
        self.assert_range_generator("(1,1)","{}")
    
    def test_range_open_one_five_open(self):
        self.assert_range_generator("(1,5)","{2,3,4}")
    
    def test_range_open_ten_fifteen_open(self):
        self.assert_range_generator("(10,15)","{11,12,13,14}")

    def test_range_open_one_five_close(self):
        self.assert_range_generator("(1,5]","{2,3,4,5}")

    def test_range_open_ten_fifteen_close(self):
        self.assert_range_generator("(10,15]","{11,12,13,14,15}")

    def test_range_close_one_five_open(self):
        self.assert_range_generator("[1,5)","{1,2,3,4}")

    def test_range_close_ten_fifteen_open(self):
        self.assert_range_generator("[10,15)","{10,11,12,13,14}")

    def test_range_close_one_five_close(self):
        self.assert_range_generator("[1,5]","{1,2,3,4,5}")

    def test_range_close_ten_fifteen_close(self):
        self.assert_range_generator("[10,15]","{10,11,12,13,14,15}")

    def test_range_close_zero_zero_close(self):
        self.assert_range_generator("[0,0]","{0}")

    def test_range_close_one_one_close(self):
        self.assert_range_generator("[1,1]","{1}")


if __name__ == '__main__':
    unittest.main()