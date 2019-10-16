class Trie:
    root = {}
    #string_dict = {}
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, str, dict):    
        if len(str) == 1:
            if str[0] not in dict:
                dict[str[0]] = 1
            else:
                dict[str[0]] = dict[str[0]] + 1                
            return
        else:
            if str[0] not in dict:
                dict[str[0]] = {}
                self.insert(str[1:], dict[str[0]])
            else:
                self.insert(str[1:], dict[str[0]])
    
    def traverse(self, dict, prefix, full_string_dict):
        string = "" 
        if len(dict) == 1 and isinstance(list(dict.values())[0] ,int):
            string = list(dict.keys())[0]
            full_string_dict[prefix + string] = list(dict.values())[0]
            return string
        else:
            for key in dict:
                self.traverse(dict[key], prefix + key, full_string_dict)
    
    def search(self, query):
        dict = self.root
        full_string_dict = {}
        for i in range(len(query)):
            if query[i] in dict:
                dict = dict[query[i]]
        
        for key in dict:
            self.traverse(dict[key], query + key, full_string_dict)
        full_string_dict = sorted(full_string_dict.items(), key=lambda d: d[1], reverse=True)       
        return full_string_dict

if __name__ == '__main__':
    trie = Trie()
    strings = ["我和我的祖国","我爱北京天安门","我爱北京天安门","我爱北京天安门","中国机长","中美贸易战","我爱北京故宫","我和我的祖国"]
    for str in strings:
        trie.insert(str, trie.root)
    print(trie.root)
    print(trie.search('我爱') )