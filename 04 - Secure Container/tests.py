import unittest
from puzzle import check_phrase, check_passwords

class TestPuzzle4(unittest.TestCase):
    def test_part_one(self):
        part = 1
        expected = 460
        actual = check_passwords(part)
        self.assertTrue(expected == actual)

    def test_part_two(self):
        part = 2
        expected = 290
        actual = check_passwords(part)
        self.assertTrue(expected == actual)
        
    def test_false_cases_part_two(self):
        part = 2
        self.assertFalse(check_phrase('123444', part))
        self.assertFalse(check_phrase('124444', part))
        self.assertFalse(check_phrase('123456', part))
        self.assertFalse(check_phrase('122222', part))

    def test_true_cases_part_two(self):
        part = 2
        self.assertTrue(check_phrase('113334', part))
        self.assertTrue(check_phrase('111334', part))
        self.assertTrue(check_phrase('113345', part))
        self.assertTrue(check_phrase('111122', part))
        self.assertTrue(check_phrase('112233', part))
        self.assertTrue(check_phrase('123445', part))

if __name__ == '__main__':
    unittest.main()
