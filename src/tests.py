import unittest
from numpy.testing import assert_array_equal
import numpy as np
from solution_007bbfb7 import solve as solve_007bbfb7
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
		 
if __name__ == '__main__':
    unittest.main()