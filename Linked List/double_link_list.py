class Node:
    def __init__(self,data):
        self.prev_node = None
        self.next_node = None
        self.data = data

    def __repr__(self):
        print(str(self.data))


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert item at end of linked list
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def traverse_forward(self):
        test_node = self.head
        while test_node is not None:
            print(test_node.data)
            test_node = test_node.next_node

    def traverse_backward(self):
        test_node = self.tail
        while test_node is not None:
            print(test_node.data)
            test_node = test_node.prev_node

    def middle_node(self):
        test1 = self.head
        test2 = self.tail
        while True:
            if test1.next_node == test2.prev_node :
                return test1
            elif test1.next_node == test2:
                return test1
            else:
                test1 = test1.next_node
                test2 = test2.prev_node

    def middle_node_two_pointers(self):
        slow_pointer = self.head
        faster_pointer = self.head
        while faster_pointer.next_node and faster_pointer.next_node.next_node :
            faster_pointer = faster_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        return slow_pointer


if __name__ == "__main__" :
    list1 = DoubleLinkedList()
    list1.insert("first")
    list1.insert("second")
    list1.insert("third")
    list1.traverse_forward()
    print()
    list1.traverse_backward()
    list2 = DoubleLinkedList()
    list2.insert("first")
    list2.insert("second")
    list2.insert("third")
    list2.insert("fourth")
    list2.insert("fifth")
    list2.insert("last")
    print()
    print(list2.middle_node().data)
    print(list2.middle_node_two_pointers().data)