"""
Single Source Shortest Path 1
単一始点最短経路
"""
INF = 1000

def dijkstra(start:int,M:list):
    N = len(M)
    p = [-1]*N
    d = [INF]*N
    color = [0]*N # 0:undiscoverd , 1:dicovered, 2:searched

    p[start] = -1
    d[start] = 0
    while True:

        mindis = INF
        for i in range(N):
            if color[i] != 2 and d[i] < mindis:
                mindis = d[i]
                u = i

        if mindis == INF:
            break
        
        color[u] = 2
        
        for v in range(N):
            if M[u][v] != INF and d[v] > d[u]+ M[u][v]:
                d[v] = d[u] + M[u][v]
                p[v] = u
                color[u] = 1

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
    adjList = [ list(map(int,input_data.pop(0).split())) for i in range(N) ]

    for i in range(N):
        adjN = adjList[i][1]
        for j in range(adjN):
            adjNode = adjList[i][j*2+2]
            M[i][adjNode] = adjList[i][j*2+3]
    
    p,d = dijkstra(0,M)

    for i in range(N):
        print(str(i)+" "+str(d[i]))

