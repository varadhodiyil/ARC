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
    def read_data(self, filename):
        data = open(filename, 'r')
        json_data = json.load(data)
        # print(json_data)
        return json_data

    def read_train(self, json_data):
        for line in enumerate(json_data['train']):
            input = line[1]['input']
            # output = line[1]['output']
            inputArr = np.asfarray(input, dtype=int)
            # outputArr = np.asfarray(output, dtype=int)
            print(inputArr)
            value_index = np.nonzero(inputArr)
            # print(value_index)
            rowindex = value_index[0]
            column_index = value_index[1]
            row_new = []
            column_new = []
            result_arr = np.zeros((6, 6))
            for var in range(len(rowindex)):
                value = inputArr[rowindex[var]][column_index[var]]
                for i in range(rowindex[var], 6):
                    row_new.append(i)
                for j in range(column_index[var], 6):
                    column_new.append(j)
                min = len(row_new)
                if (len(column_new) < len(row_new)):
                    min = len(column_new)
                for i in range(min):
                    result_arr[row_new[i]][column_new[i]] = value
                row_new = []
                column_new = []
            print(result_arr)
            d = DisplayColourImage(
                    input_array=inputArr, output_array=result_arr)
            d.display_data()


path = sys.argv[1]
print(path)
arc = ARC()
data = DataUtils(in_file=path)
json_data = data.read_data()
arc.read_train(json_data)
