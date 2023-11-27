class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_nodes = 0

    #O(1) running time complexity
    def size_list(self):
        return self.num_nodes

    #O(1) running time complexity
    def insert_initial(self,data):
        self.num_nodes += 1
        new_node = Node(data)
        # linked list is empty
        if self.head is None :
            self.head = new_node
        else:
            # node added to linked list and update the references
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self,data):
        self.num_nodes += 1
        new_node = Node(data)
        # linked list is empty
        if self.head is None :
            self.head = new_node
        else:
            # node added to end of linked list and update the references
            actual_node = self.head
            # bottleneck , O(N) runing time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            # update link of  last node to new node and make new node None
            actual_node.next_node = new_node

    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def remove(self,datainp):
        test_node = self.head
        prev_node = None

        # get to the node with data
        while (test_node is not None) and (test_node.data != datainp):
            prev_node = test_node
            test_node = test_node.next_node

        # we have moved across list till we find the data

        if test_node is None:
            # no such item
            return
        if prev_node is None:
            # found at first
            self.head = test_node.next_node
        else:
            # remove the current test node , whihc has the data
            prev_node.reference_next_node = test_node.next_node

    def reverse_linked_list(self):
        test_node = self.head
        prev_node = None
        while test_node :
            nxt_node = test_node.next_node
            # update the test node pointer
            test_node.next_node = prev_node
            prev_node = test_node
            test_node = nxt_node
        self.head = prev_node


if __name__ == "__main__":
    link1 = LinkedList()
    link1.insert_initial("first")
    link1.insert_initial("third")
    link1.insert_initial("second")
    link1.insert_initial("fourth")
    link1.traverse()
    # link1.remove(1)
    print()
    # link1.traverse()
    link1.reverse_linked_list()
    link1.traverse()