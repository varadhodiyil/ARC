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
    def read_train(self, json_data):
        for line in json_data['train']:
            input = line['input']
            output = line['output']
            inputArr = np.asfarray(input, dtype=int)
            print(inputArr)
            column_index = np.nonzero(inputArr[0, 0:])[0]
            row_index = np.nonzero(inputArr[0:, 9])[0]
            result_data = np.copy(inputArr)
            for i, j in itertools.product(row_index.tolist(), column_index.tolist()):
                result_data[i, j] = 2
            print(result_data)
            d = DisplayColourImage(
                    input_array=inputArr, output_array=result_data)
            d.display_data()

path = sys.argv[1]
print(path)
arc = ARC()
data = DataUtils(in_file=path)
json_data = data.read_data()
arc.read_train(json_data)
