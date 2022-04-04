def dfs(graph):
    visited = [0] * len(graph)
    stack = []

    stack.append(0)
    visited[0] = 1

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for i in range(len(graph)):
            if graph[s][i] == 1 and visited[i] == 0:
                 visited[i] = 1
                 stack.append(i)

dfs(
    [[0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]]
)