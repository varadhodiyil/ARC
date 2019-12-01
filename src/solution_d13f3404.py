import json
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import sys
from data_utils import DataUtils, MyExceptions
from display_colour_image import DisplayColourImage

def solve(input_array, output_array=None, graphics=False):
    assert type(input_array) == np.ndarray
    value_index = np.nonzero(input_array)
    rowindex = value_index[0]
    column_index = value_index[1]
    row_new = []
    column_new = []
    output_array = np.zeros((6, 6), dtype=int)
    for var in range(len(rowindex)):
        value = input_array[rowindex[var]][column_index[var]]
        for i in range(rowindex[var], 6):
            row_new.append(i)
        for j in range(column_index[var], 6):
            column_new.append(j)
        min = len(row_new)
        if (len(column_new) < len(row_new)):
            min = len(column_new)
        for i in range(min):
            output_array[row_new[i]][column_new[i]] = value
        row_new = []
        column_new = []
    # print(output_array)
    if graphics:
        DisplayColourImage("Solution for d13f3404",
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