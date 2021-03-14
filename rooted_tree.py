"""
Rooted Tree
根付き木の表現

id k c1 ... ckの情報が付与されたときに
節点の情報をその番号が小さい順に出力する
node id, parent , depth, type , c1 ... ck

左子右兄弟表現(left-child, right-sibling representation)
"""
from collections import namedtuple

Node = namedtuple('Node',['parent','left','right'])

if __name__ == "__main__":
    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("0 3 1 4 10")
    input_data.append("1 2 2 3")
    input_data.append("2 0")
    input_data.append("3 0")
    input_data.append("4 3 5 6 7")
    input_data.append("5 0")
    input_data.append("6 0")
    input_data.append("7 2 8 9")
    input_data.append("8 0")
    input_data.append("9 0")
    input_data.append("10 2 11 12")
    input_data.append("11 0")
    input_data.append("12 0")

    N = len(input_data)
    Tree = []
    for i in range(N):
        # 木の初期化
        node = Node(None,None,None)
        Tree.append(node)

    for data_str in input_data:
        data = data_str.split()
        tree_id = data[0]
        tree_degree = data[1]

        for i in range(tree_degree):
            child_id = data[2+tree_degree]
            if i == 0: 
                Tree[tree_id].left = child_id
            else:
                Tree[left].right = child_id
            left = child_id
            Tree[child_id].parent = tree_id
    