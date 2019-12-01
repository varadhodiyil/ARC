# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:48:49 2019

@author: Saurabh
"""
import json
import numpy as np
from data_utils import DataUtils, MyExceptions

class ARC:
    
    def read_data(self, filename):
        data = open(filename, 'r')
        json_data = json.load(data)
        #print(json_data)
        return json_data
    
    def read_train(self, json_data):
        for line in json_data['train'] + json_data['test']:
            inputData = line['input']

            inputArr = np.asfarray(inputData, dtype=int)
            result_data = self.solve(inputArr)
            #print(inputArr)        
            print(result_data)
            print("\n")

    def solve(self, input_array):
            inputArr = np.asfarray(input_array, dtype=int)
            result_data = [list(a) + list(np.flip(a)) for i,a  in enumerate(inputArr) ]
            result_data=  list(result_data)+list((np.flipud(result_data)))
            result_data = np.asarray(result_data,dtype=int)
            return result_data
        
if __name__ == "__main__":
    # main()
    import sys
    if len(sys.argv) < 2:
        raise MyExceptions("Please Specify a valid file path")
    path = sys.argv[1]
    arc = ARC()
    data = arc.read_data(filename = path)
    arc.read_train(data)

