"""
8.5 Reconstruction of the Tree

ある二分木に対して、先行順巡回と中間順巡回を行って得られる節点の列が与えられるとき、
その二分木の後行順巡回で得られる節点の列を出力せよ

"""
from collections import namedtuple
import dataclasses

Tree = []
pre_order_data = []
in_order_data = []
post_order_data = []
cnt = 0

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

def Reconstruction(l,r,d):
    global cnt
    if l < r:
        root = pre_order_data[cnt]
        cnt += 1
        m_i = in_order_data.index(root)
        left_flg,left = Reconstruction(l,m_i,cnt)
        right_flg,right = Reconstruction(m_i+1,r,cnt)

        Tree[d].value = root
        if left_flg:
            Tree[d].left = left
            Tree[left].parent = root
        if right_flg:
            Tree[d].right = right
            Tree[right].parent = root
        
        post_order_data.append(root)

        return True,d
    else:
        return False,None

if __name__ == "__main__":
    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("1 2 3 4 5")
    input_data.append("3 2 4 1 5")

    pre_order_data = [ int(i) for i in input_data[0].split() ]
    in_order_data = [ int(i) for i in input_data[1].split() ]

    N = len(pre_order_data)
    Tree = [ Node() for i in range(N) ]

    Reconstruction(0,N,0)
    print(Tree)

    print("Post Order Result:")
    print(post_order_data)

    # Treeを可視化 # graphviz
    from graphviz import Digraph

    g = Digraph(format='png')
    g.attr('node', shape='circle')
    for edge_info in Tree:
        if edge_info.parent != None:
            g.edge(str(edge_info.parent), str(edge_info.value))
    g.view()
