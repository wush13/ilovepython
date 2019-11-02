import math
class Instance:
    str = []
    label = 0
    def __init__(self, str, label):
        """
        Initialize your data structure here.
        """
        self.str = str
        self.label = label

class Term:
    term = ''
    parent_string_index = -1
    def __init__(self, term, parent_string_index):
        """
        Initialize your data structure here.
        """
        self.term = term
        self.parent_string_index = parent_string_index
    def __hash__(self):
        return 2     
    def __eq__(self, other):  ##增加eq方法默认比较引用，可以作为dict的key
        if self.term == other.term and self.parent_string_index == other.parent_string_index:
            return True
        else:
            return False

class Textset:
    instance_list = []
    tfidf_dict = {}
    tf_dict = {}
    df_dict = {}
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
    
    def calculate_tfidf(self): 
        # tf_dict = {}
        # df_dict = {}
        df_flag = {}
        index = 0
        for instance in textset.instance_list:
            string = instance.str.strip('')
            for i in range(len(string)):
                if string[i].strip() == '':
                    continue
                term = Term(string[i], index)
                if term in self.tf_dict:
                    self.tf_dict[term] +=  1.0 / len(string)
                else: 
                    self.tf_dict[term] = 1.0 / len(string)  

                if term not in df_flag:
                    if string[i] in self.df_dict:
                        self.df_dict[string[i]] += 1.0 / len(textset.instance_list)
                    else:
                        self.df_dict[string[i]] = 2.0 / len(textset.instance_list) 
                df_flag[term] = True
            index = index + 1  

        for k,v in self.tf_dict.items():
            if self.df_dict.get(k.term):
                self.tfidf_dict[k] = round(v * math.log((1.0 / self.df_dict[k.term])) ,2)

if __name__ == '__main__':
    textset = Textset()
    textset.read_data_from_file('C:/Program Files/Git/code/ilovepython/ilovepython/nlp/text.txt')
    for instance in textset.instance_list:
        print(instance.str) 
    textset.calculate_tfidf() ##calculate tfidf
    for k,v in textset.tfidf_dict.items():
        print(k.term + '\t' + str(textset.tf_dict[k]) + '\t' + str(textset.df_dict[k.term]) + '\t' + textset.instance_list[k.parent_string_index].str + '\t' + str(v))