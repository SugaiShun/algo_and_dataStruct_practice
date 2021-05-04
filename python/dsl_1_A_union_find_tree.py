"""
Disjoint Set: Union Find Tree
互いに素な集合
"""

class DisjointSet:

    rank = []
    p = []
    def __init__(self,size):
        self.rank = [0]*size
        self.p = [0]*size
        [ self.makeSet(i) for i in range(n) ]

    def makeSet(self,x:int):
        self.p[x] = x
        self.rank[x] = 0
    
    def same(self,x:int,y:int):
        return self.findSet(x) == self.findSet(y)

    def unite(self,x:int,y:int):
        self.link(self.findSet(x), self.findSet(y))
    
    def link(self,x:int,y:int):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def findSet(self,x:int):
        if x != self.p[x]: self.p[x] = self.findSet(self.p[x])
        return self.p[x]

if __name__ == "__main__":

    # n,q = map(int,input().split())

    input_data = []
    input_data.append("5 12")
    input_data.append("0 1 4")
    input_data.append("0 2 3")
    input_data.append("1 1 2")
    input_data.append("1 3 4")
    input_data.append("1 1 4")
    input_data.append("1 3 2")
    input_data.append("0 1 3")
    input_data.append("1 2 4")
    input_data.append("1 3 0")
    input_data.append("0 0 4")
    input_data.append("1 0 2")
    input_data.append("1 3 0")

    n, q = map(int,input_data.pop(0).split())
    ds = DisjointSet(n)

    for i in range(q):
        order,x,y = map(int,input_data.pop(0).split())
        if order == 0:
            ds.unite(x, y)
        else:
            ans = 1 if ds.same(x, y) else 0
            print(ans)



