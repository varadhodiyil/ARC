# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:48:49 2019

@author: Saurabh
"""




import numpy as np
import json



class ARC:
    
    def read_data(self, filename):
        data = open(filename, 'r')
        json_data = json.load(data)
        #print(json_data)
        return json_data
    
    def read_train(self, json_data):
        for line in enumerate(json_data['train']):
            inputData = line[1]['input']
            outputData = line[1]['output']
            inputArr = np.asfarray(inputData, dtype=int)
            print(inputArr)
            outputArr = np.asfarray(outputData, dtype=int)
            result_data = [list(a) + list(np.flip(a)) for i,a  in enumerate(inputArr) ]
            result_data = np.asfarray(result_data,dtype=int)
            #final = np.concatenate((inputArr, np.flip(inputArr))).tolist()
            print(result_data)
            #print(final)
            
            #print(outputArr)
  
            
            
arc = ARC()
data = arc.read_data(filename = "67e8384a.json")
arc.read_train(data)
print('done')

















