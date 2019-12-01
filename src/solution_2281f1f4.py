import json
import itertools
import numpy as np
import sys
from data_utils import DataUtils, MyExceptions
from display_colour_image import DisplayColourImage

def solve(input_array, out_array=None, graphics=False):
    assert type(input_array) == np.ndarray
    column_index = np.nonzero(input_array[0, 0:])[0]
    row_index = np.nonzero(input_array[0:, 9])[0]
    output_array = np.copy(input_array)
    for i, j in itertools.product(row_index.tolist(), column_index.tolist()):
        output_array[i, j] = 2
    # print(output_array)
    if graphics:
        DisplayColourImage("Solution for 2281f1f4",
                           input_array, output_array).display_data()
    return output_array

def main(path , graphics):

    t = DataUtils(path)
    train, test = t.train, t.test
    for _t in train + test:
        inp, out = _t['input'], _t['output']
        inp, out = np.asarray(inp), np.asarray(out)
        output_array = solve(inp, out, graphics)
        print(output_array)

if __name__ == "__main__":
    # main()
    import sys
    if len(sys.argv) < 2:
        raise MyExceptions("Please Specify a valid file path")
    else:
        path = sys.argv[1]
		
        graphics = sys.argv[2] if len(sys.argv) ==3 else False
        main(path, graphics)


    

