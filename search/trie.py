class Trie:
    root = {}
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, str, dict):    
        if len(str) == 1:
            if str[0] not in dict:
                dict[str[0]] = 'END'                
            return
        else:
            if str[0] not in dict:
                dict[str[0]] = {}
                self.insert(str[1:], dict[str[0]])
            else:
                self.insert(str[1:], dict[str[0]])

if __name__ == '__main__':
    trie = Trie()
    strings = ["我和我的祖国","我爱北京天安门","中国机长","中美贸易战","我爱北京故宫"]
    for str in strings:
        trie.insert(str, trie.root)
    print(trie.root)