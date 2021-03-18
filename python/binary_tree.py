"""
Binary Tree
根付き二分木の表現

id left rightの情報が付与されたときに
節点の情報をその番号が小さい順に出力する
node id, parent , depth, type , c1 ... ck

左子右兄弟表現(left-child, right-sibling representation)を用いる

"""
from collections import namedtuple
import dataclasses

@dataclasses.dataclass
class Node:
    parent:int = None
    left:int = None
    right:int = None
    depth:int = 0
    hegiht:int = 0
    value:int = None

def rec(r,d):
    Tree[r].depth = d
    if Tree[r].right != None:
        rec(Tree[r].right,d+1)
    if Tree[r].left != None:
        rec(Tree[r].left,d+1)

def set_hegiht(r):

    h1 = 0
    h2 = 0
    if Tree[r].right != None:
        h1 = set_hegiht(Tree[r].right) + 1
    if Tree[r].left != None:
        h2 = set_hegiht(Tree[r].left) + 1

    Tree[r].hegiht = h1 if h1 > h2 else h2

    return Tree[r].hegiht


if __name__ == "__main__":
    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("0 1 4")
    input_data.append("1 2 3")
    input_data.append("2 -1 -1")
    input_data.append("3 -1 -1")
    input_data.append("4 5 8")
    input_data.append("5 6 7")
    input_data.append("6 -1 -1")
    input_data.append("7 -1 -1")
    input_data.append("8 -1 -1")

    N = len(input_data)
    # Tree = [Node()]*N
    Tree = [ Node() for i in range(N) ]
    
    for data_str in input_data:
        data = data_str.split()
        node_id = int(data[0])
        node_left = int(data[1])
        node_right = int(data[2])
        
        Tree[node_id].value = node_id
        if node_left != -1:
            Tree[node_id].left = node_left
            Tree[node_left].parent = node_id
        if node_right != -1:
            Tree[node_id].right = node_right
            Tree[node_right].parent = node_id
    
    r_index = 0
    for i in range(N):
    # サンプルみたいに１行目に根がくるとは限らない.
    # そのため根を探す処理を入れる
        if Tree[i].parent == None:
            r_index = i
    
    rec(r_index,0)
    set_hegiht(r_index)

    print(Tree)
    
    # Treeを可視化 # graphviz
    from graphviz import Digraph

    g = Digraph(format='png')
    g.attr('node', shape='circle')
    for edge_info in Tree:
        if edge_info.parent != None:
            g.edge(str(edge_info.parent), str(edge_info.value))
    g.view()