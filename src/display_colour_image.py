import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import numpy as np

class DisplayColourImage():
    cmap=ListedColormap(['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', 
                        '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])

    def __init__(self, input_array, output_array):
        self.input_array = input_array
        self.output_array = output_array

    def display_data(self):
        fig, axes = plt.subplots(ncols=2, figsize=(8, 8))
        ax1, ax2 = axes
        input_size = self.input_array.shape[0]-1
        output_size = self.output_array.shape[0]-1
        ax1.matshow(self.input_array, vmin=0, vmax=9,  cmap=self.cmap)
        ax2.matshow(self.output_array, vmin=0, vmax=9, cmap=ListedColormap(
            ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']))
        ax1.set_xticks(np.arange(-.5, input_size, 1), minor=True)
        ax1.set_yticks(np.arange(-.5, input_size, 1), minor=True)
        ax2.set_xticks(np.arange(-.5, output_size, 1), minor=True)
        ax2.set_yticks(np.arange(-.5, output_size, 1), minor=True)
        ax1.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
        ax2.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
        plt.show()

    



