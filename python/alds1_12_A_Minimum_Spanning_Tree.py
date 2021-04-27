"""
Minimum Spanning Tree
最小全域木
"""


def prim(M:list):
    N = len(M)

    T = []
    p = [-1]*N
    color = [0]*N
    INF = 100

    u = 0

    dis = [INF]*N
    dis[0] = 0

    while True:

        min_e = INF
        for i in range(N):
            if dis[i] < min_e and color[i] != 2:
                min_e = dis[i]
                u = i
        
        if min_e == INF:
            break

        color[u] = 2

        for j in range(N):
            if M[u][j] != -1 and color[i] != 2 and M[u][j] < dis[j]:
                dis[j] = M[u][j]
                color[j] = 1
                p[j] = u

    return p

if __name__=="__main__":

    input_data=[]

    input_data.append("5")
    input_data.append("-1 2 3 1 -1")
    input_data.append("2 -1 -1 4 -1")
    input_data.append("3 -1 -1 1 1")
    input_data.append("1 4 1 -1 3")
    input_data.append("-1 -1 1 3 -1")

    N = int(input_data.pop(0))

    M = [ list(map(int,input_data.pop(0).split())) for i in range(N) ]

    p = prim(M)
