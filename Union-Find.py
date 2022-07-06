class uf_ds:
    parent_node = {}

    def set(self, u):
        for i in u:
            self.parent_node[i] = i

    def find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.find(self.parent_node[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent_node[x] = y


def display(u, data):
    print([data.find(i) for i in u])

u = [2,4,6,8]
data = uf_ds()
data.set(u)
display(u, data)
data.union(2, 8)
display(u, data)
data.union(6, 4)
display(u, data)