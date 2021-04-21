"""
Minimum Spanning Tree
最小全域木
"""
def prim(M:list):
    T = []

    N = len(M)
    u = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] != -1:
                u = j
                break
    
    T.append(u)

    return T

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

    T = prim(M)
    print(sum(T))
