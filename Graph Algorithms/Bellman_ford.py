class Edge:
    def __init__(self,weight , start_vertex , end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

class Node:
    def __init__(self,name):
        self.name = name
        self.dist = float("inf")
        self.predecessor = None
        self.adjacency_list = []

class BellmanFordAlgorithm:
    def __init__(self,vertex_list,edge_list,start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False
        self.cycle_list = []

    def  find_shortest_path(self):
        self.start_vertex.dist = 0
        for _ in range(len(self.vertex_list)-1):
            for edge in self.edge_list:
                # calculate the min distances for each node
                u = edge.start_vertex
                v = edge.end_vertex
                new_dist = u.dist + edge.weight
                if new_dist < v.dist :
                    v.dist = new_dist
                    v.predecessor = u

        # now check through edges for negative cycle
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("negative cycle in graph.....")
                vertex = edge.start_vertex
                while vertex is not edge.end_vertex:
                    self.cycle_list.append(vertex)
                    vertex = vertex.predecessor

                self.cycle_list.append(edge.end_vertex)

                for item in self.cycle_list:
                    print(item.name)

                return

    def check_cycle(self,edge):
        # if the total cost of node decreases after v-1 iterations  then
        # it has a negative cycle
        if edge.weight + edge.start_vertex.dist < edge.end_vertex.dist :
            self.has_cycle = True
            return True
        # i.e. weight is still changing for v-1 iterations
        else:
            return False

    def get_shortest_path(self,vertex):
        if not self.has_cycle:
            print(f"Shortest path to {vertex.dist}")
            node = vertex
            while node is not None:
                print(node.name)
                node = node.predecessor
        else:
            print("negative cycle in graph. NO short path")

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    edge1 = Edge(5,node1,node2)
    edge2 = Edge(9,node1,node5)
    edge3 = Edge(4,node2,node5)
    edge4 = Edge(12,node2,node3)
    edge5 = Edge(7,node2,node4)
    edge6 = Edge(3,node3,node4)
    edge7 = Edge(1,node3,node6)
    edge8 = Edge(9,node4,node7)
    edge9 = Edge(6,node5,node3)
    edge10 = Edge(4,node5,node6)
    edge11 = Edge(2,node6,node7)
    edge12 = Edge(-6,node7,node3)

    # adjacency list
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node1.adjacency_list.append(edge6)
    node1.adjacency_list.append(edge7)
    node1.adjacency_list.append(edge8)
    node1.adjacency_list.append(edge9)
    node1.adjacency_list.append(edge10)
    node1.adjacency_list.append(edge11)
    node1.adjacency_list.append(edge12)

    vertices = (node1,node2,node3,node4,node5,node6,node7)
    edges_list = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12)

    bellford = BellmanFordAlgorithm(vertices,edges_list,node1)
    bellford.find_shortest_path()
    bellford.get_shortest_path(node7)

