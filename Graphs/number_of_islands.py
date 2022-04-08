def number_of_islands(graph):
    if not graph:
        return 0

    rows, cols = len(graph), len(graph[0])
    visited = set()
    island_count = 0

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))

        while queue:
            row, col = queue.pop(0)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                if (r in range(rows) and c in range(cols) and graph[r][c] == 1 and (r, c) not in visited):
                    queue.append((r, c))
                    visited.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if graph[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                island_count += 1

    return island_count

print(number_of_islands([[1,1,1,1,0], 
                        [1,1,0,1,0], 
                        [1,1,0,0,0], 
                        [0,0,1,0,1]]))
