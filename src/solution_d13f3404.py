import json
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap


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
            # for i,j in itertools.product(range(1,11), range(1,11)):
            # 	print(str(i) + ":" + str(j))
            # cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', segmentdata=cdict,N=256)
            fig, axes = plt.subplots(ncols=2, figsize=(8, 8))
            ax1, ax2 = axes

            ax1.matshow(inputArr, vmin=0, vmax=8,  cmap=ListedColormap(
                ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']))
            ax2.matshow(result_arr, vmin=0, vmax=8, cmap=ListedColormap(
                ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']))
            # plt.colorbar()
            ax1.set_xticks(np.arange(-.5, 3, 1), minor=True)
            ax1.set_yticks(np.arange(-.5, 3, 1), minor=True)
            # ax1.Text('Inut')
            ax2.set_xticks(np.arange(-.5, 6, 1), minor=True)
            ax2.set_yticks(np.arange(-.5, 6, 1), minor=True)
            ax1.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
            ax2.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
            plt.show()


arc = ARC()
data = arc.read_data(filename="data/training/d13f3404.json")

arc.read_train(data)
print('done')
