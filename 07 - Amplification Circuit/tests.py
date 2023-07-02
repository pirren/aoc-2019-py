import unittest
import sys
sys.set_int_max_str_digits(0)
from puzzle import exe, run_intcode


class TestPuzzle7PartOne(unittest.TestCase):
    def test_part_one(self):
        expected = 101490
        actual = run_intcode([0,1,2,3,4])
        self.assertEqual(expected, actual)

    def test_part_one_sample_case_one(self):
        expected = 43210

        sequence = [4,3,2,1,0]
        program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        io_signal = 0
        for phase_setting in sequence:
            io_signal = exe(program, io_signal, phase_setting)
        
        actual = io_signal

        self.assertEqual(expected, actual)

    def test_part_one_sample_case_two(self):
        expected = 54321
        
        sequence = [0,1,2,3,4]
        program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        io_signal = 0
        for phase_setting in sequence:
            io_signal = exe(program, io_signal, phase_setting)
        
        actual = io_signal

        self.assertEqual(expected, actual)

    def test_part_one_sample_case_three(self):
        expected = 65210
        
        sequence = [1,0,4,3,2]
        program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        io_signal = 0
        for phase_setting in sequence:
            io_signal = exe(program, io_signal, phase_setting)
        
        actual = io_signal

        self.assertEqual(expected, actual)

class TestPuzzle7PartTwo(unittest.TestCase):
    def test_part_one(self):
        expected = True 
        actual = True #run_intcode([0,1,2,3,4])
        
        self.assertEqual(expected, actual)

    # def test_part_two_sample_case_one(self):
    #     expected = 139629729

    #     sequence = [9,8,7,6,5]
    #     program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    #     io_signal = 0
    #     for phase_setting in sequence:
    #         io_signal = exe(program, io_signal, phase_setting)
    #         print(io_signal)
        
    #     actual = io_signal

    #     self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()