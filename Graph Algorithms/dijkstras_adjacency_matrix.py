import sys

class DijkstrasAdjacencyMatrix:
    def __init__(self,adjacency_matrix,start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        # stores actual minimum value
        self.visited = [False for _ in range(self.v)]
        self.distance = [float("inf") for _ in range(self.v)]
        self.distance[start_vertex] = 0

    def get_min_vertex(self):
        # find vertex with lowest value
        min_vertex_value = sys.maxsize
        min_vertex_index = 0
        # O(N) to get vertex with minimum value and its index
        # this  can also be done with heap in log N time
        for index in range(self.v):
            if not self.visited[index] and self.distance[index] < min_vertex_value :
                min_vertex_value = self.distance[index]
                min_vertex_index = index
        return min_vertex_index

    def calculate(self):
        for vertex in range(self.v):
            test_index = self.get_min_vertex()
            print(f"consider vertex {test_index}")
            self.visited[test_index] = True
            for other_vertex in range(self.v):
                if self.adjacency_matrix[test_index][other_vertex] > 0:
                    if self.distance[test_index] + self.adjacency_matrix[test_index][other_vertex] < \
                            self.distance[other_vertex]:
                        self.distance[other_vertex] = self.distance[test_index] + self.adjacency_matrix[test_index][other_vertex]
                        # above updates the minmum distance value for node
                        # that has not been visited and derived value is less than current min distance

    def print_distance(self):
        print(self.distance)

if __name__ == '__main__':

    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = DijkstrasAdjacencyMatrix(m, 1)
    algorithm.calculate()
    algorithm.print_distance()














