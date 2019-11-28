import json
import numpy as np


class Train():

	def __init__(self,in_file="007bbfb7.json"):
		self.data = self.read_data(in_file)
		self.train , self.test = self.data['train'] , self.data['test']


	def _train(self):
		
		for i in self.train:
			elements = i['input']
			print(elements)
			result = np.zeros((9,9))
			loop = 0
			for r_cnt,r in enumerate(elements):
				for c_cnt,e in enumerate(r):
					
					print(loop)
					if e !=0:
						for _r in range(3):
							for _c in range(3):
								print(r_cnt + _r, r_cnt + (loop*3) + _c )
								# result[r_cnt + _r] [c_cnt + _c + loop +1 ] = elements[_r][_c]
					loop = loop + 1
			# print(result)
	

t = Train("data/training/007bbfb7.json")
# print(t)
t._train()
