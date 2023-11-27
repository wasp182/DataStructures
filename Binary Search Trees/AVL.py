class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left_node = None
        self.right_node = None

class AVL:
    def __init__(self):
        self.root = None

    def remove(self,data):
        if self.root :
            self.remove_node(data,self.root)

    def remove_node(self,data,node):
        if node is None:
            return
        if node.data > data :
            self.remove_node(data,node.left_node)
        elif node.data < data:
            self.remove_node(data,node.right_node)
        else:
            # node to be remove if found here
            # Case 1 : node is leaf node
            if node.left_node is None and node.right_node is None :
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                elif parent is not None and parent.right_node == node :
                    parent.right_node = None
                # single root leaf case
                if parent is None :
                    self.root = None
                del node
                self.handle_violation(parent)
            # case 2 :  subtree on one side : on right side
            elif node.left_node is None and node.right_node is not None :
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node
                if parent is None:
                    self.root = None
                node.right_node.parent = parent
                del node
                self.handle_violation(parent)
            # case 2 :  subtree on one side : on left side
            elif node.right_node is None and node.left_node is not None :
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                if parent is None:
                    self.root = None
                node.left_node.parent = parent
                del node
                self.handle_violation(parent)
            else:
                # Case 3 : node has subtree on both sides
                # replace the node with predecessor
                predecessor = self.get_predecessor(node.left_node)
                predecessor.data , node.data = node.data , predecessor.data
                self.remove_node(data,predecessor)

    def get_predecessor(self,node):
        if node.right_node:
            self.get_predecessor(node.right_node)
        return node

    def insert(self,data):
        if self.root is None:
            self.root = Node(data,parent=None)
        else:
            self.insert_node(data,self.root)

    def insert_node(self,data,node):
        if data > node.data :
            if node.right_node :
                self.insert_node(data,node.right_node)
            else:
                # look for leaf nodes
                node.right_node = Node(data,node)
                node.height = max(self.calculate_height(node.left_node),self.calculate_height(node.right_node))+ 1
        else:
            # look for leaf nodes
            if node.left_node:
                self.insert_node(data,node.left_node)
            else:
                # add new node once leaf nodes are found
                node.left_node = Node(data,node)
                node.height = max(self.calculate_height(node.left_node),self.calculate_height(node.right_node))+ 1
        # check for violation of balance tree
        self.handle_violation(node)

    def calculate_height(self,node):
        if node is None:
            return -1
        return node.height

    def calculate_balance(self,node):
        if node is None:
            return 0
        else:
            return self.calculate_height(node.left_node) - self.calculate_height(node.right_node)

# check all nodes till root nodes if they are balanced
    def handle_violation(self,node):
        while node is not None:
            node.height = max(self.calculate_height(node.left_node),self.calculate_height(node.right_node))+1
            # check if tree is balanced or not
            self.violation_helper(node)
            node = node.parent


# Checks if tree is balanced or not at given node
    def violation_helper(self,node):
        balance = self.calculate_balance(node)
        if balance > 1:
            # left heavy , right rotation is required. It might be left right heavy or left left heavy
            if self.calculate_balance(node.left_node) < 0 :
                # left rotation on parent and right rotation on grandparent. \
                # If left-right heavy , we need to make left rotation on parent
                self.rotate_left(node.left_node)
            # if left-left heavy or left right ,  right rotation on grandparent has to be made
            self.rotate_right(node)
        if balance < -1 :
            # right heavy , left rotation is required. If left right heavy then additional right rotation on grandparent
            if self.calculate_balance(node.right_node) > 0 :
                self.rotate_right(node.right_node)
            # left rotation no matter what
            self.rotate_left(node)

    def rotate_left(self,node):
        print("rotating Left {}".format(node.data))
        # Node C and D (child and grandchild) saved as they will be modified
        temp_right_node = node.right_node
        temp_grandchild_left = temp_right_node.left_node
        # UPDATE NODE_D 'S LEFT NODE AS NODE_B (NODE)
        temp_right_node.left_node = node
        # UPDATE NODE_B 'S RIGHT AS TEMP_GRANCHILD
        node.right_node = temp_grandchild_left

        # UPDATE PARENTS OF NODES B,C,D
        # Updating Node C's parents as Node B
        if temp_grandchild_left:
            temp_grandchild_left.parent = node
        temp_parent = node.parent
        # update Node B's parents as Node D
        node.parent = temp_right_node
        # updating Node D's parents with B's parent
        temp_right_node.parent = temp_parent

        # UPDATE PARENTS OF NODES B,C,D TO CHECK IF NODE IS LEFT OR RIGHT OF B'S PARENT
        #UPDATE node D
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node
        # UPDATE node B
        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node :
            temp_right_node.parent.left_node = temp_right_node
        if node == self.root:
            self.root = temp_right_node
        node.height = max(self.calculate_height(node.left_node),self.calculate_height(node.right_node))+ 1
        temp_right_node.height = max(self.calculate_height(temp_right_node.left_node),self.calculate_height(temp_right_node.right_node)) + 1

    def rotate_right(self,node):
        print("rotating Right {}".format(node.data))
        # Node B and C saved as they will be modified
        temp_left_node = node.left_node
        temp_grandchild_right = temp_left_node.right_node

        # update node B
        node.left_node = temp_grandchild_right
        # Update Node C
        temp_left_node.right_node = node

        ################### Update parents of node B,C and D###########
        # Update Parents of C
        if temp_grandchild_right:
            temp_grandchild_right.parent = node
        # store parents of main node D
        temp_parent = node.parent
        # update parents of D
        node.parent = temp_left_node
        # Update parents of B
        temp_left_node.parent = temp_parent

        # Notify parents of D ( main node)
        #TODO modification here
        if temp_parent is not None and temp_parent.left_node == node:
            temp_parent.left_node = temp_left_node
        if temp_parent is not None and temp_parent.right_node == node:
            temp_parent.right_node = temp_left_node

        ################ Update heights #############################
        node.height = max(self.calculate_height(node.left_node),self.calculate_height(node.right_node))+ 1
        temp_left_node.height = max(self.calculate_height(temp_left_node.left_node),self.calculate_height(temp_left_node.right_node)) + 1

    def traversal(self):
        if self.root:
            self.traversal_in_order(self.root)

    def traversal_in_order(self,node):
        if node.left_node:
            self.traversal_in_order(node.left_node)
        # print Left , Right and parent of a node while traversing
        l,r,p = "","",""
        if node.left_node is not None:
            l = node.left_node.data
        else:
            l = "Null"
        if node.right_node is not None:
            r = node.right_node.data
        else:
            r="Null"
        if node.parent:
            p = node.parent.data
        else:
            p = "Null"
        print(f" Data:{node.data} , Left Node:{l} , Right Node:{r} , Parent:{p} ")
        if node.right_node:
            self.traversal_in_order(node.right_node)

if __name__ == "__main__":
    avl=AVL()
    avl.insert(5)
    avl.insert(3)
    # avl.insert(6)
    avl.insert(1)

    # avl.remove(6)
    avl.traversal()