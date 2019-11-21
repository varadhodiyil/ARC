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
			column_index = np.nonzero(inputArr[0,0:])[0]
			row_index = np.nonzero(inputArr[0:,9])[0]
			result_data = inputArr
			for i,j in itertools.product(row_index.tolist(), column_index.tolist()):
				result_data[i,j] = 2
			print(result_data)
			print(outputArr)
			
			if (np.array_equal(outputArr, result_data)):
				print('Correct result')
			else:
				print('wrong')
			# cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', segmentdata=cdict,N=256)
			plt.matshow(result_data, cmap=ListedColormap(['black', 'red', 'grey']))
			plt.show()
arc = ARC()
data = arc.read_data(filename = "data/training/2281f1f4.json")

arc.read_train(data)
print('done')
