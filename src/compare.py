import os
import json


r = open('2.json','r')
test_file = json.load(r)

# test_file_str = json.dumps(test_file,indent=4)
for r,_,files in os.walk('data/training'):
    for f in files:

        # 
        _file_name = os.path.join(r,f)
        # _file_name = "data\\training\\bda2d7a6.json"
        inFile = open(_file_name,'r')
        iterFile = json.load(inFile)
        test_train = test_file['train']
        inter_train = iterFile['train']
        cnt = len(test_train)
        flag = 0
        for i, t in enumerate(test_train):
            try:
                # print(test_train[i].values())

                # print('*' *10)
                # print( inter_train[i].values()) 
                # break
                
                if sorted(list(t.values())) == sorted(list(inter_train[i].values())):
                    flag += 1
            except IndexError:
                continue
        if cnt == flag:
            print(f)
        # print(json.dumps(test_train, indent=4), json.dumps(inter_train,indent=4))
        # iterFile_str = json.dumps(iterFile,indent=4)
        



        # break