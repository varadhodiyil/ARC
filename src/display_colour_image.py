import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import numpy as np


class DisplayColourImage():
    cmap = ListedColormap(['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA',
                           '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])

    def __init__(self, name, input_array, output_array):
        self.name = name
        self.input_array = input_array
        self.output_array = output_array

    def display_data(self):
        fig, axes = plt.subplots(ncols=2, figsize=(8, 8))
        ax1, ax2 = axes
        fig.suptitle('Task ' + self.name)
        ax1 = self.set_plot(ax1, self.input_array, 'Input Grid')
        ax2 = self.set_plot(ax2, self.output_array, 'Output Grid')
        plt.show()

    def set_plot(self, axis, array, title):
        size = array.shape[0]
        axis.matshow(array, vmin=0, vmax=9,  cmap=self.cmap)
        axis.set_xticks(np.arange(-.5, size, 1), minor=True)
        axis.set_yticks(np.arange(-.5, size, 1), minor=True)
        axis.set_xticklabels([])
        axis.set_yticklabels([])
        axis.set_title(title)
        axis.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
        return axis
