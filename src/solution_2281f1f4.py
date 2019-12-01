import json
import itertools
import numpy as np
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
        column_index = np.nonzero(input_array[0, 0:])[0]
        row_index = np.nonzero(input_array[0:, 9])[0]
        output_array = np.copy(input_array)
        for i, j in itertools.product(row_index.tolist(), column_index.tolist()):
            output_array[i, j] = 2
        return output_array

if (len(sys.argv) < 2):
    raise MyExceptions("Please provide path in the command line python <python-filename> <json-path> <display-image>")
else:
    path = sys.argv[1]
display_image = False
if(len(sys.argv) > 2):
    display_image = sys.argv[2]
arc = ARC(display_image = display_image, path = path)

