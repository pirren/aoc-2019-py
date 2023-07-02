import unittest
from puzzle import part_one, part_two

class TestPuzzle3(unittest.TestCase):
    def test_part_one_answer(self):
        actual = part_one()
        expected = 273
        self.assertEquals(actual, expected)

    def test_part_two_answer(self):
        actual = part_two()
        expected = 15622
        self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()