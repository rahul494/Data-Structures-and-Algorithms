def bfs(graph):
    queue = []
    visited = [0] * len(graph)
    
    queue.append(0) # start at first node
    visited[0] = 1

    while queue:
        curr = queue.pop(0)
        print(curr, end = " ")

        for i in range(len(graph)):
            if graph[curr][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

bfs(
    [[0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]]
)