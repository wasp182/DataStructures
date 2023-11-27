class Node:
    def __init__(self,data , parent = None):
        self.left_node = None
        self.right_node = None
        self.data = data
        # useful for remove operation
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        # BST is not empty
        else:
            self.insert_node(data,self.root)

    # recursive implementation of insert_node
    def insert_node(self,data,node):
        if data > node.data :
            if node.right_node :
                self.insert_node(data,node.right_node)
            else:
                node.right_node = Node(data,node)
        else:
            if node.left_node:
                self.insert_node(data,node.left_node)
            else:
                node.left_node = Node(data,node)

    def get_min(self):
        # underlying BST is empty
        if self.root is None:
            return None
        # iterate through nodes
        elif self.root.left_node :
            min_node = self.root.left_node
            while min_node.left_node :
                min_node = min_node.left_node
            return min_node.data
        else:
            return self.root.data

    def get_max(self):
        # underlying BST is empty
        if self.root is None:
            return None
        # iterate through nodes
        elif self.root.right_node :
            max_node = self.root.right_node
            while max_node.right_node :
                max_node = max_node.right_node
            return max_node.data
        else:
            return self.root.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self,node):
        # travel left subtree , then root and then right subtree
        if node.left_node:
            self.traverse_in_order(node.left_node)
        # if there is no more left node then print node , this prints the root node of subtree
        print(node.data)
        if node.right_node:
            self.traverse_in_order(node.right_node)

    def remove(self,data):
        if self.root:
            self.remove_node(self.root,data)

    def remove_node(self,node,data):
        if node is None:
            return
        if data < node.data:
            self.remove_node(node.left_node , data)
        elif data > node.data :
            self.remove_node(node.right_node , data)
        else:
            # we have found the correct node - this node could be leaf node
            # or could be single child , or two child nodes
            if node.left_node is None and node.right_node is None:
                # Case 1 : this is leaf node
                print("removing leaf node {}".format(node.data))
                parent = node.parent
                if parent is not None and parent.left_node == node :
                    parent.left_node = None
                if parent is not None and parent.right_node == node :
                    parent.right_node = None
                if parent is None:
                    self.root = None
                del node

            # Case 2 : when there is a single child
            elif node.left_node is None and node.right_node is not None:
                print("removing node with single right child")
                parent = node.parent
                if parent is not None and parent.left_node == node :
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node :
                    parent.right_node = node.right_node
                if parent is None:
                    self.root = None
                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("removing node with single left chile")
                parent = node.parent
                if parent is not None and parent.left_node == node :
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node :
                    parent.right_node = node.left_node
                if parent is None:
                    self.root = None
                node.left_node.parent = parent
                del node
            else: # Case 3 :  remove node with two child
                print("removing node with two children")
                predecessor = self.get_predecessor(self,node.left_node)
                # replace actual node with predecessor and remove the actual node which would be a leaf
                # as predecessor is a leaf node
                # swap and remove predecessor
                predecessor.data , node.data = node.data , predecessor.data
                self.remove_node(predecessor,data)



    def get_predecessor(self,node):
        # get maximum of the tree i.e. right most value
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(10)
    # bst.insert(145)
    # bst.insert(15)
    # bst.insert(-21)
    bst.traverse()
    print("***Remove Operation***")
    bst.remove(148)
    bst.remove(10)
    print("*****")
    bst.traverse()
    print("Max Min")
    print(bst.get_max())
    print(bst.get_min())