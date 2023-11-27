import heapq

class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.distance = float("inf")
        # stores node closest to given node for minimal spanning tree
        self.predecessor = None
        self.visited = False

    def __lt__(self, other):
        return self.distance < other.distance

def djikstras_alg(start_node,end_node):
    heap = []
    start_node.distance = 0
    heapq.heappush(heap,(start_node.distance,start_node))

    while heap:
        dist , test_node = heapq.heappop(heap)
        if test_node.visited :
            continue
        for edge,node in test_node.adjacency_list:
            if node.distance > ( test_node.distance + edge ):
                node.distance = test_node.distance + edge
                node.predecessor = test_node
            heapq.heappush(heap,(node.distance,node))
        test_node.visited = True

    if end_node:
        print(f" minimal distance is : {end_node.distance}")
        print_path(end_node)
        return end_node.distance
    else:
        print("end node is not in graph")

def print_path(end_node):
    test = end_node.predecessor
    while test :
        print(test.name , test.distance)
        test = test.predecessor

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node1.adjacency_list.append((5,node2))
    node1.adjacency_list.append((8,node8))
    node1.adjacency_list.append((9,node5))
    node2.adjacency_list.append((4,node8))
    node2.adjacency_list.append((12,node3))
    node2.adjacency_list.append((15,node4))
    node8.adjacency_list.append((7,node3))
    node8.adjacency_list.append((6,node6))
    node5.adjacency_list.append((5,node8))
    node5.adjacency_list.append((4,node6))
    node5.adjacency_list.append((20,node7))
    node3.adjacency_list.append((3,node4))
    node3.adjacency_list.append((11,node7))
    node6.adjacency_list.append((1,node3))
    node6.adjacency_list.append((13,node7))
    node4.adjacency_list.append((9,node7))
    djikstras_alg(node1,node7)