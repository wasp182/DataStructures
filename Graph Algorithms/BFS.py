class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):
    queue = [start_node]
    start_node.visited = True
    # keep iterating over neighbours till queue is not empty
    while queue :
        # we use pop to ensure that list is adjusted for removing item from queue
        # O(N) run time
        test_node = queue.pop(0)
        print(test_node.name)
        for neighbour_node in test_node.adjacency_list:
            if neighbour_node.visited is False:
                neighbour_node.visited = True
                queue.append(neighbour_node)

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node2.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node3.adjacency_list.append(node4)

    breadth_first_search(node1)











