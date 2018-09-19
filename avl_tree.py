class AvlTree(object):

    def __init__(self, root=None):
        self.root = root

    def search(self, val):
        return self._do_search(val, self.root)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)  
        else:
            self._do_insert(val, self.root)

    def delete(self, val):
        pass

    def inorder_traversal(self):
        self._do_inorder_traversal(self.root)

    def _do_search(self, val, node):
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._do_search(val, node.left)
        else:
            return self._do_search(val, node.right)

    def _do_insert(self, val, node):
        if node.left == None and node.val >= val:
            node.left = TreeNode(val)
        elif node.right == None and node.val <= val:
            node.right = TreeNode(val)
        else:
            self._do_insert(val, node.left if node.val >= val else node.right)
            balance = self._get_balance(node)
            if balance < -1:
                self._rotate_right(node)
            elif balance > 1:
                self._rotate_left(node)

    def _get_balance(self, node):
        return self._get_max_depth(node.right) - self._get_max_depth(node.left)

    def _rotate_right(self, node):
        node_left = node.left
        node_right = node.right
        node_val = node.val

        node.val = node_left.val
        node.left = node_left.left
        node.right = TreeNode(node_val)
        node.right.left = node_left.right
        node.right.right = node_right

    def _rotate_left(self, node):
        node_left = node.left
        node_right = node.right
        node_val = node.val
        
        node.val = node_right.val
        node.right = node_right.right
        node.left = TreeNode(node_val)
        node.left.right = node_right.left
        node.left.left = node_left

    def _get_max_depth(self, node):
        if node is None:
            return 0

        return 1 + max(self._get_max_depth(node.left), self._get_max_depth(node.right))

    def _do_inorder_traversal(self, node):
        if node is not None:
            if node.left is not None:
                self._do_inorder_traversal(node.left)

            print(node.val)

            if node.right is not None:
                self._do_inorder_traversal(node.right)

    def __str__(self):
        root = str(self.root.val) if self.root is not None else ""
        left = str(self.root.left.val) if self.root is not None and self.root.left is \
not None else ""
        right = str(self.root.right.val) if self.root is not None and self.root.right \
is not None else ""
        return "AvlTree(root=%s, left=%s, right=%s)" % (root, left, right)

class TreeNode(object):
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':

    tree = AvlTree()
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)
    tree.insert(11)
    tree.insert(5)
    tree.insert(1)

    print(tree)

    tree.inorder_traversal()
