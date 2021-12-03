class MagicDictionary:

    def __init__(self):
        self.dic = None

    def buildDict(self, dictionary):
        self.dic = dictionary

    def search(self, searchWord):
        for word in self.dic:
            diff = 0
            if len(word) != len(searchWord):
                continue
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff += 1
            if diff == 1:
                print(True)
                return True
        print(False)
        return False


magicDictionary = MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello");
magicDictionary.search("hhllo");
magicDictionary.search("hell");
magicDictionary.search("leetcoded")
