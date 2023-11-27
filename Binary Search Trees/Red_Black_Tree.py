class Color:
    red = 1
    black = 2

class Node:
    def __init__(self,data,parent = None, color = Color.red):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.color = color
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root :
            self.insert_node(data,self.root)
        else:
            self.root = Node(data)
            self.violation_handler(self.root)

    def insert_node(self,data,node):
        if data > node.data:
            if node.right_node :
                self.insert_node(data,node.right_node)
            else:
                node.right_node = Node(data,parent=node)
                self.violation_handler(node.right_node)
        else:
            if node.left_node:
                self.insert_node(data,node.left_node)
            else:
                node.left_node = Node(data,parent=node)
                self.violation_handler(node.left_node)

    def violation_handler(self,node):
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            parent_node = node.parent
            grandparent_node = parent_node.parent
            # check if parent is left or right child of grandparent
            if parent_node == grandparent_node.left_node:
                uncle_node = grandparent_node.right_node
                # Check case 1 and 4 as they require recoloring
                if uncle_node and self.is_red(uncle_node):
                    print(f"recolor Grandparent to red : {grandparent_node.data}")
                    grandparent_node.color = Color.red
                    print(f"recolor parent and uncle to black : {parent_node.data} and {uncle_node.data}")
                    parent_node.color = Color.black
                    uncle_node.color = Color.black
                    node = grandparent_node
                else:
                    # case 2 and 3 : Uncle is black
                    # case 2 : Node is right child
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        # parent node is modified and we need to check if new node is leading to violations
                        node = parent_node
                        parent_node = node.parent
                    else:
                        # case 3 :  Node is left child
                        if node == parent_node.left_node:
                            print(f"recolor grandparent node to red : {grandparent_node.data}")
                            grandparent_node.color = Color.red
                            print(f"recolor parent to black : {parent_node.data}")
                            parent_node.color = Color.black
                            self.rotate_right(grandparent_node)
            else:
                # Check the above operations for symmetric case
                # Uncle is left node instead
                uncle_node = grandparent_node.left_node
                # Case 1 and 4 for recoloring
                if uncle_node and self.is_red(uncle_node):
                    print(f"recolor grandparent node to red: {grandparent_node.data}")
                    grandparent_node.color = Color.red
                    print(f"recoloring parent and uncle node to black : {parent_node.data} & {uncle_node.data}")
                    parent_node.color = Color.black
                    uncle_node.color = Color.black
                    node = grandparent_node
                else: # Case 2 and 3 : uncle node is black and left node of grandparent
                    # Case 2 : node is left node of parent
                    if node == parent_node.left_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    else:
                        # Case 3 : node is right node of parent
                        if node == parent_node.right_node:
                            print(f"recolor grandparent node to red : {grandparent_node.data}")
                            grandparent_node.color = Color.red
                            print(f"recolor parent to black : {parent_node.data}")
                            parent_node.color = Color.black
                            self.rotate_left(grandparent_node)
        if self.is_red(self.root):
            print(f"recolor  root to black : {self.root.data}")
            self.root.color = Color.black

    def is_red(self,node):
            if node is None:
                return False
            return node.color == Color.red

    def traverse(self):
        if self.root:
            self.traversal_in_order(self.root)

    def traversal_in_order(self,node):
        if node.left_node:
            self.traversal_in_order(node.left_node)
        print(f"Data : {node.data} left node : {node.left_node.data} right node : {node.right_node.data} color: {node.color}")
        if node.right_node:
            self.traversal_in_order(node.right_node)

    def rotate_right(self,node):
        print(f"Rotating right at node: {node.data}")
        temp_left_node = node.left_node
        temp_grandchild_right = temp_left_node.right_node

        #update the nodes values
        temp_left_node.right_node = node
        node.left_node = temp_grandchild_right

        # update parents
        if temp_grandchild_right :
            temp_grandchild_right.parent = node

        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node

        # update the parent orientation of new main node
        if temp_parent and temp_left_node.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
        if temp_parent and temp_left_node.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self,node):
        print(f"Rotating left at node: {node.data}")
        temp_right_node = node.right_node
        temp_grandchild_left = temp_right_node.left_node

        #update the nodes values
        temp_right_node.left_node = node
        node.right_node = temp_grandchild_left

        # update parents
        if temp_grandchild_left :
            temp_grandchild_left.parent = node

        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node

        # update the parent orientation of new main node
        if temp_parent and temp_right_node.left_node == node:
            temp_right_node.parent.left_node = temp_right_node
        if temp_parent and temp_right_node.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(32)
    tree.insert(20)
    tree.insert(55)
    tree.insert(1)
    tree.insert(19)
    tree.insert(79)
    tree.insert(16)
    tree.insert(23)
    tree.insert(12)
    print("*"*80)
    # tree.traverse()








