class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def edge(self, u, v, w):
        self.graph.append([u, v, w])
    def subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.subtree(parent, parent[i])
    def union(self, parent, rank, x, y):
        xroot = self.subtree(parent, x)
        yroot = self.subtree(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.subtree(parent, u)
            y = self.subtree(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.edge(0, 1, 4)
g.edge(0, 2, 4)
g.edge(1, 2, 2)
g.edge(1, 0, 4)
g.edge(2, 0, 4)
g.edge(2, 1, 2)
g.edge(2, 3, 3)
g.edge(2, 5, 2)
g.edge(2, 4, 4)
g.edge(3, 2, 3)
g.edge(3, 4, 3)
g.edge(4, 2, 4)
g.edge(4, 3, 3)
g.edge(5, 2, 2)
g.edge(5, 4, 3)
g.algo()