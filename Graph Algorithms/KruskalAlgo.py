class Vertex:
    def __init__(self,name):
        # this class represents vertices in graph
        self.name = name
        # below are the nodes in disjoint set
        self.node = None

class Edge:
    def __init__(self, weight,start_vertex,end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    # comparing edges for sorting purpose of Kruskal Algo
    def __lt__(self, other):
        return self.weight < other.weight

class Node:
    # this is class for disjoint data structure underlying the Kruskal algo
    def __init__(self,node_id,rank,parent=None):
        # node id stores the index position in root node as it is added to disjoint set
        self.node_id = node_id
        # rank is basically the height in BST
        self.rank = rank
        self.parent = parent

class DisjointSet:
    def __init__(self,vertex_list):
        self.vertex_list = vertex_list
        # representatives of disjoint set
        self.root_nodes = []
        # make sets of all vertices in graph
        self.make_sets()

    def find(self,node):
        # find representative of root node i.e. root node and apply path compression
        # to ensure all nodes in set are pointing to same root node i.e. representative value
        # returns index or id of root node of given node
        current_node = node
        while current_node.parent is not None:
            current_node = current_node.parent

        # apply path compression for purpose of O(1) running time
        root = current_node

        # re initialise to node and map all paths in set to root node
        current_node = node
        # all nodes in set to point at root node
        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp
        return root.node_id

    def merge(self,node1,node2):
        # check index of root nodes , if they are same index then they
        # belong to same disjoint set
        node1_index = self.find(node1)
        node2_index = self.find(node2)
        # check rank of each node to combine smaller to root of larger rank
        # if the nodes are in same set then do not add to disjoint set
        if node1_index == node2_index:
            return
        # checking ranks if not part of same set
        # access root node value through index of root list
        node1_root = self.root_nodes[node1_index]
        node2_root = self.root_nodes[node2_index]
        if node1_root.rank < node2_root.rank:
            node1_root.parent = node2_root
        elif node1_root.rank > node2_root.rank:
            node2_root.parent = node1_root
        else:
            node2_root.parent = node1_root
            # update the rank of one of the parent
            # we don't need this in two other cases as one of root index is already
            # larger and can accommodate at least one addition else it would have been equal
            node1_root.rank += 1

    def make_sets(self):
        for v in self.vertex_list:
            node = Node(len(self.root_nodes),0,parent=None)
            v.node = node
            self.root_nodes.append(node)

class KruskalAlgorithm:
    def __init__(self,vertex_list,edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_mst(self):
        disjoint_set = DisjointSet(self.vertex_list)
        mst = []
        # step 1 - sort edges by weight from vertex list
        self.edge_list.sort()

        # step 2 - consider min weight edge , do union of end and start node
        # add the edge to mst if nodes are not part of same set and merge them
        # into same set
        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.end_vertex
            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                # add edge to list of mst
                mst.append(edge)
                disjoint_set.merge(u.node,v.node)
        # print all edges in MST
        for edge in mst:
            print(f"Edge between : {edge.start_vertex.name} and {edge.end_vertex.name}. Edge weight : {edge.weight}")

if __name__ =="__main__":
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    edge1 = Edge(2,vertex1,vertex2)
    edge2 = Edge(6,vertex1,vertex3)
    edge3 = Edge(5,vertex1,vertex5)
    edge4 = Edge(10,vertex1,vertex6)
    edge5 = Edge(3,vertex2,vertex4)
    edge6 = Edge(3,vertex2,vertex5)
    edge7 = Edge(1,vertex3,vertex4)
    edge8 = Edge(2,vertex3,vertex6)
    edge9 = Edge(4,vertex4,vertex5)
    edge10 = Edge(5,vertex4,vertex7)
    edge11= Edge(5,vertex6,vertex7)

    # have to create list of edges and vertices
    vertices = []
    vertices.append(vertex1)
    vertices.append(vertex2)
    vertices.append(vertex3)
    vertices.append(vertex4)
    vertices.append(vertex5)
    vertices.append(vertex6)
    vertices.append(vertex7)

    edge_list=[]
    edge_list.append(edge1)
    edge_list.append(edge2)
    edge_list.append(edge3)
    edge_list.append(edge4)
    edge_list.append(edge5)
    edge_list.append(edge6)
    edge_list.append(edge7)
    edge_list.append(edge8)
    edge_list.append(edge9)
    edge_list.append(edge10)
    edge_list.append(edge11)

    # algorithm
    alg = KruskalAlgorithm(vertices,edge_list)
    alg.find_mst()