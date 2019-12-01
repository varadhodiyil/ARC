from data_utils import DataUtils, MyExceptions
import json
import numpy as np


def solve(in_arr, out_arr=None):
	assert type(in_arr) == np.ndarray
	in_arr_shape = in_arr.shape
	result = np.zeros((in_arr_shape[1]**2, in_arr_shape[1]**2), dtype=int)
	a, b = in_arr_shape[0], in_arr_shape[1]
	for row_idx, _row in enumerate(in_arr):
		for col_idx, element in enumerate(_row):
			if element == 0:
				continue
			else:
				for row in range(a):
					for col in range(b):
						result[(row_idx*a) + row][(col_idx*b) +
													col] = in_arr[row][col]
	print(result)
	return result


def main(path):

    t = DataUtils(path)
    train, test = t.train, t.test
    for _t in train + test:
        inp, out = _t['input'], _t['output']
        inp, out = np.asarray(inp), np.asarray(out)
        solve(inp, out)

    # print(t)
    # t._train()


if __name__ == "__main__":
    # main()
    import sys
    if len(sys.argv) < 2:
        raise MyExceptions("Please Specify a valid file path")
    else:
        path = sys.argv[1]
        main(path)
