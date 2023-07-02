import unittest
from puzzle import run_intcode

class TestPuzzle5(unittest.TestCase):
    def test_part_one(self):
        expected = 5182797
        actual = run_intcode(None, 1)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 12077198
        actual = run_intcode(None, 5)
        self.assertEqual(expected, actual)

    def test_part_two_sample_position_mode_input_eight_equals_eight_returns_one(self):
        program = [3,9,8,9,10,9,4,9,99,-1,8]
        expected = 1
        actual = run_intcode(program, 8)
        self.assertEqual(expected, actual)

    def test_part_two_sample_position_mode_input_less_than_eight_returns_one(self):
        program = [3,9,7,9,10,9,4,9,99,-1,8]
        expected = 1
        actual = run_intcode(program, 7)
        self.assertEqual(expected, actual)

    def test_part_two_sample_immediate_mode_input_equal_to_eight_returns_one(self):
        program = [3,3,1108,-1,8,3,4,3,99]
        expected = 1
        actual = run_intcode(program, 8)
        self.assertEqual(expected, actual)

    def test_part_two_sample_immediate_mode_input_less_than_eight_returns_one(self):
        program = [3,3,1107,-1,8,3,4,3,99]
        expected = 1
        actual = run_intcode(program, 7)
        self.assertEqual(expected, actual)

    def test_part_two_sample_position_mode_jump_input_zero_returns_zero(self):
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        expected = 0
        actual = run_intcode(program, 0)
        self.assertEqual(expected, actual)

    def test_part_two_sample_position_mode_jump_input_non_zero_returns_one(self):
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        expected = 1
        actual = run_intcode(program, 1)
        self.assertEqual(expected, actual)

    # The large example program uses an input instruction to ask for a single number. 
    # The program will then output 999 if the input value is below 8, 
    # output 1000 if the input value is equal to 8, 
    # or output 1001 if the input value is greater than 8
    def test_part_two_large_sample_position_mode_jump_input_non_zero_returns_one(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        
        expected = [x for x in range(999, 1002)]
        actual = [run_intcode(program, x) for x in range(7, 10)]

        for i in range(0,3):
            self.assertEqual(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()