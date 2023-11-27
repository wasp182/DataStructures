from BST_1 import BinarySearchTree

class TreeComparator:
    def compare(self, node1, node2):
        # check base case - these nodes maybe None
        if not node1 or not node2:
            return node1 == node2
        # check values in node
        if node1.data is not node2.data :
            return False
        # check left and right nodes recursively
        return self.compare(node1.left_node , node2.left_node) and \
               self.compare(node1.right_node,node2.right_node)


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert(1)
    bst1.insert(10)
    bst1.insert(145)
    bst1.insert(15)
    bst1.insert(-21)
    bst1.traverse()
    bst2 = BinarySearchTree()
    bst2.insert(1)
    bst2.insert(10)
    bst2.insert(145)
    bst2.insert(15)
    bst2.insert(-21)
    bst2.traverse()
    print(TreeComparator.compare(bst1.root,bst2.root))
