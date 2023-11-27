class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def depth_first_Search(start_node):
    stack = [start_node]
    start_node.visited = True
    while stack:
        # pop item return last item inserted
        test_node = stack.pop()
        print(test_node.name)
        # iterate through its neighbours
        for node in test_node.adjacency_list:
            if not node.visited:
                test_node.visited = True
                stack.append(node)


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    depth_first_Search(node1)