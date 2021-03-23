"""
Binary Search Tree
二分探索木
動的な集合を取り扱うデータ構造として連結リストがあるが、
要素を探索するにはO(n)の計算量を必要とする
より効率的に追加・削除・探索をするのに二分探索木がある
各節点にキーを持ち、二分探索木条件を常に満たす
二分探索木条件は以下である
・ある節点xにおける左部分木yは(yのキー <=  xのキー）を満たす
・ある節点xにおける右部分木zは(xのキー <=  zのキー）を満たす

"""
import dataclasses

Tree = []
pre_order_data = []
in_order_data = []
post_order_data = []

root_node = None

@dataclasses.dataclass
class Node:
    key:int = None
    parent:int = None
    left:int = None
    right:int = None

def insert(new_node:Node):
    parent_node = None
    r_node = root_node

    while r_node!= None:
        parent_node = r_node
        if r_node.key <= new_node.key:
            r_node = r_node.left
        else:
            r_node = r_node.right
    
    new_node.parent = parent_node
    if parent_node == None:
        root_node = new_node

    if new_node.key <= parent_node.key:
        parent_node.left = new_node
    else:
        parent_node.right = new_node

if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("32")
    input_data.append("12")
    input_data.append("40")

    for node_data in input_data:
        new_node = Node(key=int(node_data))
        insert(new_node)

    data

    while 
    print()
