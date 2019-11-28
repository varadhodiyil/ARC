# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:48:49 2019

@author: Saurabh
"""


import numpy as np
import json

#arr1 = [[1, 6, 6], [5, 2, 2], [2, 2, 2]]
arr1 = [[5, 3, 4], [3, 4, 5], [3, 4, 4]]


c = [a + list(np.flip(np.asarray(a))) for i, a in enumerate(arr1)]
#d = [a + list(np.flip(np.asarray(a))) for i,a  in enumerate(arr1) ]
#d = (np.flip(np.asarray(c)))
# print(np.concatenate(c,d))
print("C", c)
final = np.concatenate((c, np.flip(c))).tolist()
print(np.concatenate((c, np.flip(c))))
print(json.dumps(final))


"""
{"test": 
[{"input": [[1, 6, 6], [5, 2, 2], [2, 2, 2]], 
"output": [[1, 6, 6, 6, 6, 1], [5, 2, 2, 2, 2, 5], [2, 2, 2, 2, 2, 2], 
		   [2, 2, 2, 2, 2, 2], [5, 2, 2, 2, 2, 5], [1, 6, 6, 6, 6, 1]]}],
"""

"""
"train": 
[{"input": [[5, 3, 4], [3, 4, 5], [3, 4, 4]], 
"output":  [[5, 3, 4, 4, 3, 5], [3, 4, 5, 5, 4, 3], [3, 4, 4, 4, 4, 3], 
            [3, 4, 4, 4, 4, 3], [3, 4, 5, 5, 4, 3], [5, 3, 4, 4, 3, 5]]},
"""
