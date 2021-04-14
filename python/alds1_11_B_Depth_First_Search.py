"""
Depth First Search
深さ優先探索
"""

import alds1_3_A_basic_dataStruct as originalStack

N = 0
nt = 0
M = 0

def vList2vMatrix(input_data):
    g_mat = [ [0]*len(input_data) for i in range(len(input_data)) ]

    for v_list in input_data:
        v_list = v_list.split()

        v_i = int(v_list[0]) - 1
        v_adj_num = int(v_list[1])
        for i in range(v_adj_num):
            v_adj = int(v_list[i+2]) - 1
            g_mat[v_i][v_adj] = 1

    return g_mat

def next(u):
    for v in range(nt[u],N):
        nt[u] = v + 1
        if M[u][v]: return v
    return -1

if __name__ == "__main__":


    input_data=[]

    input_data.append("6")
    input_data.append("1 2 2 3")
    input_data.append("2 2 3 4")
    input_data.append("3 1 5")
    input_data.append("4 1 6")
    input_data.append("5 1 6")
    input_data.append("6 0")

    N = int(input_data.pop(0))
    M = vList2vMatrix(input_data)
    color = [0]*N
    d = [0]*N
    f = [0]*N
    s = originalStack.stack()
    time = 1

    nt = [0]*N

    s.push(0)
    color[0] = 1
    d[0] = time
    while not(s.is_empty()):
        u = s.top()
        v = next(u)
        if v != -1:
            if color[v] == 0:
                color[v] = 1
                time += 1
                d[v] = time
                s.push(v)
        else:
            s.pop()
            color[u] = 2
            time += 1
            f[u] = time


    print("output:{}".format(d))
    print("output:{}".format(f))
