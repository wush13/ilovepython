from dataset import Dataset
import math
import numpy as np
class Logistic:
    weights_x = []
    rate = 0.0
    iteration_cnt = 0
    #string_dict = {}
    def __init__(self, rate, length, iteration_cnt ):
        """
        Initialize your data structure here.
        """
        self.rate = rate 
        self.weights_x = np.random.rand(length)
        self.iteration_cnt = iteration_cnt
    def sigmoid(self, e):
        return 1 / (1 + math.exp(-e))

    def classify(self, data_x):
        if len(data_x) != len(self.weights_x):
            return 0
        value = 0.0
        for i in range(len(data_x)):
            value += float(data_x[i]) * float(self.weights_x[i])
        return self.sigmoid(value)

    def train_sd(self, instance_list):
        for k in range(self.iteration_cnt):
            gd = np.random.rand(len(self.weights_x))
            for instance in instance_list:
                data = instance.data
                label = instance.label
                calculate_label = self.classify(data)
                for j in range(len(data)):
                    gd[j] =  self.rate * (float(calculate_label) - float(label)) * float(data[j])
            for j in range(len(data)):
                self.weights_x[j] += gd[j] 
            print("iteration " + str(k))
            print(self.weights_x)    


if __name__ == '__main__':
    logistic = Logistic(0.001, 6, 10)
    dataset = Dataset()
    dataset.read_data_from_file('ds.txt')
    for instance in dataset.instance_list:
        print(instance.data)
        print(instance.label)
    logistic.train_sd(dataset.instance_list)