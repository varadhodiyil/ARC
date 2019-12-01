import unittest
from numpy.testing import assert_array_equal
import numpy as np
from solution_007bbfb7 import solve as solve_007bbfb7 
from Solution_67e8384a import ARC
class TestARC(unittest.TestCase):

	def test_007bbfb7(self):
		in_arr = np.array([[4, 0, 4], 
			[0, 0, 0], 
			[0, 4, 0]])
		result = solve_007bbfb7(in_arr)
		out_arr = [[4, 0, 4, 0, 0, 0, 4, 0, 4], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 4, 0, 0, 0, 0, 0, 4, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 4, 0, 4, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 4, 0, 0, 0, 0]]

		assert_array_equal(result,out_arr)
	
	def test_67e8384a(self):
		in_arr = np.array([[1, 6, 6], [5, 2, 2], [2, 2, 2]])
		result = ARC().solve(in_arr)
		out_arr = [
		 [1, 6, 6, 6, 6, 1],
		 [5, 2, 2, 2, 2, 5], 
		 [2, 2, 2, 2, 2, 2], 
		 [2, 2, 2, 2, 2, 2], 
		 [5, 2, 2, 2, 2, 5], 
		 [1, 6, 6, 6, 6, 1]]

		assert_array_equal(result,out_arr)
		 
if __name__ == '__main__':
    unittest.main()