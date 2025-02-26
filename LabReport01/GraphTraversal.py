import numpy as np

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = float('inf')
        self.topoOrder = []
        self.visited = None  

    def init(self):   
        while True:
            N = np.random.randint(4, 8)
            print("grid size:", N)
            graph = np.random.randint(0, 2, (N, N))
            print("graph:\n", graph)
            self.N = N
            self.visited = np.zeros((N, N), dtype=bool)
            sourceX, sourceY = np.random.randint(0, N), np.random.randint(0, N)
            goalX, goalY = np.random.randint(0, N), np.random.randint(0, N)
            if graph[sourceX][sourceY] == 1 and graph[goalX][goalY] == 1:
                self.source = Node(sourceX, sourceY, 0)
                self.goal = Node(goalX, goalY, self.goal_level)
                print("source:", (sourceX, sourceY))
                print("goal:", (goalX, goalY))
                self.st_dfs(graph, self.source)
                if self.found:
                    print("goal found  moves", self.goal.depth)
                else:
                    print("goal cannot starting block")
                print("topological :", self.topoOrder)
                return
            else:
                print("invalid source")

    def print_direction(self, m, x, y):
        moves = ["down", "up", "right", "left"]
        print(f"moving {moves[m]} ({x}, {y})")

    def st_dfs(self, graph, u):
        self.visited[u.x][u.y] = True  
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1 and not self.visited[v_x][v_y]:
                self.print_direction(j, v_x, v_y)
                v_depth = u.depth + 1
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
                if self.found:
                    return
        self.topoOrder.append((u.x, u.y))  
    
def main():
    d = DFS()
    d.init()
if __name__ == "__main__":
    main()