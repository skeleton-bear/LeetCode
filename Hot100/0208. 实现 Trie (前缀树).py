# 很重要
class TrieNode:
    def __init__(self):
        # childern 是一个字典,key是一个字符,value是下一个TrieNode
        self.childern = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树插入一个单词
        """
        current = self.root
        for char in word:
            # 如果字符不在当前节点的子节点中,为他创建一个新节点
            if char not in current.childern:
                current.childern[char] = TrieNode()
            current = current.childern[char]

        current.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        """
        查找一个完整的单词是否存在
        """
        current = self.root
        for char in word:
            if char not in current.childern:
                return False
            current = current.childern[char]

        return  current.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        查找是否存在以某个前缀开头的单词。
        """
        current = self.root
        for char in prefix:
            # 如果路径中某个字符不存在，说明此前缀不存在
            if char not in current.childern:
                return False
            current = current.childern[char]
            
        # 只要能走完前缀的路径，就说明存在
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)