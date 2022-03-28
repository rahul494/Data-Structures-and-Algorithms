class Graph:
    def __init__(self, graph):
        self.graph = graph
    
    def dfs(self, node):
        visited = [node]
        stack = [node]

        while stack:
            s = stack.pop()
            print(s, end = " ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

adjacency_list = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : ['G'],
  'G' : []
}

graph = Graph(adjacency_list)
graph.dfs('A')