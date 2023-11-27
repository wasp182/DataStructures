class TravellingSalesmanProblem:
    def __init__(self,graph):
        self.graph = graph
        # no of vertices in grpah
        self.n_vertices = len(self.graph)
        self.visited = [False for _ in range(self.n_vertices)]
        # start with first vertex
        self.visited[0] = True
        # collect hamiltonian cycles
        self.hamiltonian_cycle = []
        # add vertices to hamiltonian
        self.path = [0 for _ in range(self.n_vertices)]

    def is_valid(self,vertex,actual_position):
        # actual position is node being visited
        if self.visited[vertex]:
            return False
        # check for connection between vertex and actual_position
        if self.graph[vertex][actual_position] == 0 :
            return False
        return True

    def tsp(self,actual_position,counter,cost):
        # check if cycle is completed
        if counter== self.n_vertices and self.graph[actual_position][0]:
            # this is a hamiltonian path
            self.path.append(0)
            print(self.path)
            # current position complete the cycle to
            self.hamiltonian_cycle.append([cost+self.graph[actual_position][0]])
            self.path.pop()
            return

        # consider nodes in G(V,E and filter out non adjacent nodes
        for i in range(self.n_vertices):
            if self.is_valid(i,actual_position):
                self.visited[i] = True
                self.path[counter] = i
                # counter is tracking no of vertices included in path
                self.tsp(i,counter+1,cost+self.graph[actual_position][i])
                # now we backtrack , since there is no cycle if we continue after above
                # recursive call we set visit back to false
                self.visited[i] = False

if __name__ == "__main__":
    g =[[0,1,0,2,0],[1,0,1,0,2],[0,1,0,3,1],[2,0,3,0,1],[0,2,1,1,0]]
    tsp = TravellingSalesmanProblem(g)
    tsp.tsp(0,counter=1,cost=0)
    print(tsp.hamiltonian_cycle)









