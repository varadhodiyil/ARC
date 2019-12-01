import json
import os
import datetime


class MyExceptions(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message

    def __str__(self):
        return "Uh -huh {0} Error Occured at {1}" .format(self.message, datetime.datetime.now())


class DataUtils():
    def __init__(self, in_file=None):
        self.in_file = in_file
        self.get_train_test()

    @property
    def train(self):
        return self.__train

    @property
    def test(self):
        return self.__test

    def read_data(self, in_file=None):
        if self.in_file is None and in_file is None:
            raise MyExceptions("Please specify input file please")
        data_file = self.in_file if self.in_file else in_file
        if not os.path.exists(data_file):
            raise MyExceptions("File Doesn't exist")
        f = open(data_file, "r")
        self.data = json.load(f)
        return self.data

    def get_train_test(self):
        data = self.read_data()
        self.__train, self.__test = data['train'], data['test']


if __name__ == '__main__':

    d = DataUtils(in_file="../data/training/d13f34041.json")

    d.read_data()
