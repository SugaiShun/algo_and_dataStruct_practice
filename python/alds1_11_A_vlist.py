"""
Graph
グラフ

隣接リストから隣接行列を出力する
"""
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

if __name__ == "__main__":


    input_data=[]

    input_data.append("1 2 2 4")
    input_data.append("2 1 4")
    input_data.append("3 0")
    input_data.append("4 1 3")

    output = vList2vMatrix(input_data)
    print("output:{}".format(output))
