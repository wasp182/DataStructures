import heapq

class Vertex:
    def __init__(self,name):
        self.name = name
        # adjacency list of edges that surround a given graph
        self.adjacency_list = []


class Edge:
    def __init__(self,weight,start_vertex,end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsJarnik:
    def __init__(self,unvisited_list):
        self.unvisited_list = unvisited_list
        # if unvisited list becomes empty , we terminate the alg
        self.mst = []
        self.total_cost = 0
        self.heap = []

    def find_spanning_tree(self,start_vertex):
        self.unvisited_list.remove(start_vertex)
        test_vertex = start_vertex
        # we won't update the content of heap basis any new edge added to heap
        # this is the lazy implementation
        while self.unvisited_list:
            for edge in test_vertex.adjacency_list:
                if edge.end_vertex in self.unvisited_list:
                    heapq.heappush(self.heap,edge)
                    # push vertex to heap and check for minimum weight in heap
                    # this is simply the root node of heap
            min_weight_edge = heapq.heappop(self.heap)
            if min_weight_edge.end_vertex in self.unvisited_list:
                self.mst.append(min_weight_edge)
                print(f"Adding edge to spanning tree : {min_weight_edge.start_vertex.name} to {min_weight_edge.end_vertex.name}")
                self.total_cost += min_weight_edge.weight
                test_vertex = min_weight_edge.end_vertex
                # remove vertex to be visited next
                self.unvisited_list.remove(test_vertex)

    def get_total_cost(self):
        return self.total_cost


if __name__ == "__main__":
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")

    # dealing with undirected edges
    # undirected edge = directed edge (u,v) + directed edge (v,u)
    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]

    vertexA.adjacency_list.append(edgeAB)
    vertexA.adjacency_list.append(edgeAC)
    vertexA.adjacency_list.append(edgeAE)
    vertexA.adjacency_list.append(edgeAF)
    vertexB.adjacency_list.append(edgeBA)
    vertexB.adjacency_list.append(edgeBD)
    vertexB.adjacency_list.append(edgeBE)
    vertexC.adjacency_list.append(edgeCA)
    vertexC.adjacency_list.append(edgeCD)
    vertexC.adjacency_list.append(edgeCF)
    vertexD.adjacency_list.append(edgeDB)
    vertexD.adjacency_list.append(edgeDC)
    vertexD.adjacency_list.append(edgeDE)
    vertexD.adjacency_list.append(edgeDG)
    vertexE.adjacency_list.append(edgeEA)
    vertexE.adjacency_list.append(edgeEB)
    vertexE.adjacency_list.append(edgeED)
    vertexF.adjacency_list.append(edgeFA)
    vertexF.adjacency_list.append(edgeFC)
    vertexF.adjacency_list.append(edgeFG)
    vertexG.adjacency_list.append(edgeGD)
    vertexG.adjacency_list.append(edgeGF)

    # run the algorithm
    algorithm = PrimsJarnik(unvisited_list)
    algorithm.find_spanning_tree(vertexD)
    print(algorithm.get_total_cost())
