class Graph:
    def __init__(self):
        self.graph = {}
    def addCity(self, city, nextCity, cost):
        self.graph[city] = (nextCity, cost)

graph = Graph()
graph.addCity("benguerrir", "youssoufia", 100)
graph.addCity("youssoufia", "marrakech", 300)
graph.addCity("marrakech", "benguerrir", 200)
graph.addCity("safi", "", 100)

visited = set()
def dfs(visited, graph, city):
    if city not in visited:
        print(city)
        visited.add(city)
        dfs(visited, graph, graph[city][0])

dfs(visited, graph.graph, "youssoufia")
