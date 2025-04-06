def is_safe(node, color, graph, colors, c):
    for neighbor in graph[node]:
        if colors[neighbor] == c:
            return False
    return True

def solve(node, graph, colors, N, K):
    if node == N:
        return True
    for c in range(1, K + 1):
        if is_safe(node, color, graph, colors, c):
            colors[node] = c
            if solve(node + 1, graph, colors, N, K):
                return True
            colors[node] = 0
    return False

def graph_coloring(N, M, K, edges):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * N

    if solve(0, graph, colors, N, K):
        print(f"Coloring Possible with {K} Colors")
        print(f"Color Assignment: {colors}")
    else:
        print(f"Coloring Not Possible with {K} Colors")

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline()
        N, M, K = map(int, first_line.strip().split())
        edges = []
        for _ in range(M):
            u, v = map(int, file.readline().strip().split())
            edges.append((u, v))
    return N, M, K, edges

if __name__ == "__main__":
    filename = "input.txt"  
    N, M, K, edges = read_input_from_file(filename)
    graph_coloring(N, M, K, edges)

