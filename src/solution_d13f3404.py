import json
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import sys
from data_utils import DataUtils, MyExceptions
from display_colour_image import DisplayColourImage

class ARC:

    def __init__(self, display_image=False, path=None):
        self.display_image = display_image
        self.path = path
        self.train()
        
    def train(self):
        data = DataUtils(in_file=path)
        train, test = data.get_Train_Test()
        json_name = path.split("\\")[len(path.split("\\"))-1]
        for _t in train + test:
            input_data, output_data = _t['input'], _t['output']
            input_array, output_array = np.asfarray(input_data), np.asfarray(output_data)
            result_array = self.solve(input_array)
            print('Input Grid')
            print(input_array)
            print('Output Grid')
            print(output_array)
            if (display_image):
                d = DisplayColourImage(
                        name=json_name, input_array=input_array, output_array=result_array)
                d.display_data()
            
    def solve(self, input_array):
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
        return output_array


if (len(sys.argv) < 2):
    raise MyExceptions("Please provide path in the command line python <python-filename> <json-path> <display-image>")
else:
    path = sys.argv[1]
display_image = False
if(len(sys.argv) > 2):
    display_image = sys.argv[2]
arc = ARC(display_image = display_image, path = path)