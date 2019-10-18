
import numpy as np
class Instance:
    data = []
    label = 0
    def __init__(self, data, label):
        """
        Initialize your data structure here.
        """
        self.data = data
        self.label = label

class Dataset:
    instance_list = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instance_list = []
    def read_data_from_file(self, filename):
        file1 = open(filename,'r')
        lines = file1.readlines()
        for line in lines:
            arr = line.replace('\n', '').split('\t')
            if len(arr) <= 2:
                break
            else:
                instance = Instance(arr[1:], arr[0])
                self.instance_list.append(instance)

if __name__ == '__main__':
    dataset = Dataset()
    dataset.read_data_from_file('ds.txt')
    for instance in dataset.instance_list:
        print(instance.data)
        print(instance.label)