import unittest
from puzzle import part_one, part_two

class TestPuzzle2(unittest.TestCase):
    def test_part_one(self):
        result_part_one = part_one()
        self.assertEquals(result_part_one, 3166704)

    def test_part_two(self):
        result_part_two = part_two()
        self.assertEquals(result_part_two, 8018)

if __name__ == '__main__':
    unittest.main()