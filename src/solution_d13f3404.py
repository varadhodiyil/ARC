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
        for line in enumerate(json_data['train']):
            input = line[1]['input']
            input_array = np.asfarray(input, dtype=int)
            output_array = self.solve(input_array)
            print(input_array)
            print(output_array)
            d = DisplayColourImage(
                    name=json_name, input_array=input_array, output_array=output_array)
            d.display_data()
            
    def solve(self, input_array):
        value_index = np.nonzero(input_array)
        rowindex = value_index[0]
        column_index = value_index[1]
        row_new = []
        column_new = []
        output_array = np.zeros((6, 6))
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


path = sys.argv[1]
print(path)
json_name = path.split("\\")[len(path.split("\\"))-1]
arc = ARC()
data = DataUtils(in_file=path)
json_data = data.read_data()
arc.train(json_name, json_data)

