"""
Single Source Shortest Path 2
単一始点最短経路（ダイクストラをヒープで高速化）
"""
import heapq

INF = 1000

def dijkstra(start:int,adjList:list):
    N = len(M)
    p = [-1]*N
    d = [INF]*N
    color = [0]*N # 0:undiscoverd , 1:dicovered, 2:searched

    p[start] = -1
    d[start] = 0

    h = [(0,0)]
    heapq.heapify(h)
    while len(h)>0:

        mindis,u = heapq.heappop(h) # first factor is used for heap
        color[u] = 2
        
        for i,v in enumerate(adjList[u]):
            if i%2==0:
                if color[v] == 2: continue
                if d[v] > d[u]+ adjList[u][i+1]:
                    d[v] = d[u] + adjList[u][i+1]
                    p[v] = u
                    color[u] = 1
                    heapq.heappush(h, (d[v],v))

    return p,d

if __name__=="__main__":
    input_data=[]

    input_data.append("5")
    input_data.append("0 3 2 3 3 1 1 2")
    input_data.append("1 2 0 2 3 4")
    input_data.append("2 3 0 3 3 1 4 1")
    input_data.append("3 4 2 1 0 1 1 4 4 3")
    input_data.append("4 2 2 1 3 3")

    N = int(input_data.pop(0))
    M = [ [INF]*N for i in range(N) ]
    adjList = [ list(map(int,input_data.pop(0).split()[2:])) for i in range(N) ]
    
    p,d = dijkstra(0,adjList)

    for i in range(N):
        print(str(i)+" "+str(d[i]))


