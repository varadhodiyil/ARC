import json
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import sys
from data_utils import DataUtils
from display_colour_image import DisplayColourImage


class ARC:
    def train(self, json_name, json_data):
        for line in json_data['train']:
            input_data = line['input']
            output_data = line['output']
            input_array = np.asfarray(input_data, dtype=int)
            output_array = self.solve(input_array)
            print('INPUT')
            print(input_array)
            print('OUTPUT')
            print(output_array)
            d = DisplayColourImage(
                name=json_name, input_array=input_array, output_array=output_array)
            d.display_data()
    
    def solve(self, input_array):
        column_index = np.nonzero(input_array[0, 0:])[0]
        print(type(column_index))
        row_index = np.nonzero(input_array[0:, 9])[0]
        output_array = np.copy(input_array)
        for i, j in itertools.product(row_index.tolist(), column_index.tolist()):
            output_array[i, j] = 2
        return output_array

path = sys.argv[1]
print(path)
json_name = path.split("\\")[len(path.split("\\"))-1]
arc = ARC()
data = DataUtils(in_file=path)
json_data = data.read_data()
arc.train(json_name, json_data)
