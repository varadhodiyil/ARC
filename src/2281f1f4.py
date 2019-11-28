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
            output = line[1]['output']
            inputArr = np.asfarray(input, dtype=int)
            outputArr = np.asfarray(output, dtype=int)
            print(inputArr)
            column_index = np.nonzero(inputArr[0, 0:])[0]
            row_index = np.nonzero(inputArr[0:, 9])[0]
            result_data = np.copy(inputArr)
            for i, j in itertools.product(row_index.tolist(), column_index.tolist()):
                result_data[i, j] = 2
            print(result_data)
            print(outputArr)

            if (np.array_equal(outputArr, result_data)):
                print('Correct result')
            else:
                print('wrong')
            # cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', segmentdata=cdict,N=256)
            fig, axes = plt.subplots(ncols=2, figsize=(8, 8))
            ax1, ax2 = axes

            ax1.matshow(inputArr, vmin=0, vmax=9,  cmap=ListedColormap(
                ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']))
            ax2.matshow(result_data, vmin=0, vmax=9, cmap=ListedColormap(
                ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']))
            # plt.colorbar()
            ax1.set_xticks(np.arange(-.5, 9, 1), minor=True)
            ax1.set_yticks(np.arange(-.5, 9, 1), minor=True)
            # ax1.Text('Inut')
            ax2.set_xticks(np.arange(-.5, 9, 1), minor=True)
            ax2.set_yticks(np.arange(-.5, 9, 1), minor=True)
            ax1.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
            ax2.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
            plt.show()


arc = ARC()
data = arc.read_data(filename="data/training/2281f1f4.json")

arc.read_train(data)
print('done')
