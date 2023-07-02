import unittest
from puzzle import part_one, part_two

class TestPuzzle6PartOne(unittest.TestCase):
    def test_part_one_solution(self):
        expected = 204521
        actual = part_one()
        self.assertEqual(expected, actual)

class TestPuzzle6PartTwo(unittest.TestCase):
    def test_part_two_solution(self):
        expected = 307
        actual = part_two()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()