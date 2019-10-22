
class Instance:
    data = []
    label = 0
    def __init__(self, data, label):
        """
        Initialize your data structure here.
        """
        self.data = data
        self.label = label

class Textset:
    instance_list = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instance_list = []
    def read_data_from_file(self, filename):
        file1 = open(filename,encoding='utf-8')
        lines = file1.readlines()
        for line in lines:
            arr = line.replace('\n', '').split('\t')
            if len(arr) == 1:
                instance  = Instance(arr[0], -1)
                self.instance_list.append(instance)
            elif len(arr) == 2:
                instance = Instance(arr[0], arr[1])
                self.instance_list.append(instance)

if __name__ == '__main__':
    textset = Textset()
    textset.read_data_from_file('text.txt')
    for instance in textset.instance_list:
        print(instance.data) 