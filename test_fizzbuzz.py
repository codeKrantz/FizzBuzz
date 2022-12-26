from fizzbuzz import FizzBuzz
import unittest


class TestFizzBuzz(unittest.TestCase):


    def test_fizzbuzz_method_return_fizz_for_three(self):
        self.assertEqual("Fizz", FizzBuzz().fizzbuzz(3))

    def test_fizzbuzz_method_return_one_for_one(self):
        self.assertEqual("1", FizzBuzz().fizzbuzz(1))

    def test_fizzbuzz_method_return_buzz_for_five(self):
        self.assertEqual("Buzz", FizzBuzz().fizzbuzz(5))
        
    def test_fizzbuzz_method_return_fizzbuzz_for_fifteen(self):
        self.assertEqual("FizzBuzz", FizzBuzz().fizzbuzz(15))
        
if __name__ == '__main__':
    unittest.main()  # pragma: no cover
