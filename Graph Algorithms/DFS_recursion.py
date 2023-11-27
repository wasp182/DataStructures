class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list =[]
        self.visited = False

def depth_first_search(start_node):
    # recursive implementation
    # take start node , add neighbours
    # this node is visited
    start_node.visited = True
    print(start_node.name)
    # take neighbours of start node and run DFS recursively through them
    for nodes in start_node.adjacency_list:
        if not nodes.visited:
            depth_first_search(nodes)

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

    depth_first_search(node1)