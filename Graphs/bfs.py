class Graph:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, node):
        visited = [node]
        queue = [node]
        
        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
            
        

adjacency_list = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

graph = Graph(adjacency_list)
graph.bfs('A')