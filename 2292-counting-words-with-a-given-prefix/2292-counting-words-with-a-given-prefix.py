class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
    def count_prefix(self, pref): 
        node = self.root
        for char in pref:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count


class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.count_prefix(pref)
        