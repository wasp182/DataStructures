from collections import deque

class MazeSovler:
    def __init__(self,matrix):
        self.matrix = matrix
        self.visited =[ [False for _ in range(len(matrix))] for _ in range(len(matrix))]
        # first entry of move x and move y imply right move , second entries upward (-1 is up , 1 is down for y list)
        self.move_x = [1,0,0,-1]
        self.move_y = [0,-1,1,0]
        self.min_dist = float("inf")

    def is_valid(self,row,col):
        if row < 0 or row >= len(self.matrix):
            return False
        # outside table vertically
        if col < 0 or col >= len(self.matrix):
            return False
        if self.matrix[row][col] == 0:
            return False
        if self.visited[row][col] == True:
            return False
        return True

    def search(self,i,j,destination_x,destination_y):
        # using BFS
        self.visited[i][j] = True
        queue = deque()
        # third item is distance
        queue.append((i,j,0))
        while queue:
            # FIFO access
            (i,j,dist) = queue.popleft()
            if i == destination_x and j == destination_y:
                self.min_dist = dist
                break
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                if self.is_valid(next_x,next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x,next_y,dist+1))

    def show_results(self):
        if self.min_dist != float("inf"):
            print("Shortest path is {}".format(self.min_dist))
        else:
            print("No solution")


if __name__ == "__main__":

    adj_matrix = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    maze = MazeSovler(adj_matrix)
    maze.search(0,0,4,4)
    maze.show_results()