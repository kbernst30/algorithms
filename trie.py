class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        self._do_insert(self.root, word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        w = word
        next_node = self.root
        while len(w) != 0:
            next_node = next_node.get_child(w[0])
            if next_node is None:
                return False

            print(next_node)
            w = w[1:]

        print([n.value for n in next_node.children])
        return not next_node.has_children()

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        w = prefix
        next_node = self.root
        while len(w) != 0:
            next_node = next_node.get_child(w[0])
            if next_node is None:
                return False

            w = w[1:]

        return True

    def _do_insert(self, node, word):
        if len(word) != 0:
            next_node = node.get_child(word[0])
            if next_node is not None:
                self._do_insert(next_node, word[1:])
            else:
                w = word
                next_node = node
                while len(w) != 0:
                    next_node.add_child(w[0])
                    next_node = next_node.get_child(w[0])
                    w = w[1:]


class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def has_children(self):
        return len(self.children) > 0

    def add_child(self, child):
        self.children.append(TrieNode(child))

    def get_child(self, child):
        for i in range(len(self.children)):
            if self.children[i].value == child:
                return self.children[i]

        return None


if __name__ == '__main__':
    obj = Trie()
    print(obj.insert("apple"))
    print("SEARCH")
    print(obj.search("apple"))
