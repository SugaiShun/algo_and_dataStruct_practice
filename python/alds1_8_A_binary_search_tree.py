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
cnt = 0

@dataclasses.dataclass
class Node:
    key:int = None
    parent:int = None
    left:int = None
    right:int = None

def insert(Tree,new_node):
    parent = None
    root = 0
