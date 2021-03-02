"""
Koch Curve
整数nを入力し、深さnの再帰呼び出しによって作成される
コッホ曲線の頂点の座標を出力する

コッホ曲線は再帰的な構造をもつ図形であるフラクタルの一種である
・与えられた線分（p1,p2）を３等分する
・線分を３等分する２点s,tを頂点とする正三角形(s,u,t)を作成する
線分(p1,s),線分(s,u),線分(u,t),線分(t,p2)に対して再起的に同じ操作を繰り返す

端点(0,0)から開始し、一方の端点(100,0)で
終える一続きの線分の列となる順番に出力せよ
"""
from collections import namedtuple
import math

Point = namedtuple('Point',('x','y'))

def koch_curve(d,p1:Point,p2:Point):

    if d == 0:
        return None

    sx = (2*p1.x + p2.x)/3
    sy = (2*p1.y + p2.y)/3
    s = Point(sx,sy)
    tx = (p1.x + 2*p2.x)/3
    ty = (p1.y + 2*p2.y)/3
    t = Point(tx,ty)

    theta = math.radians(60)
    ux = (t.x - s.x)*math.cos(theta) - (t.y - s.y)*math.sin(theta) + s.x
    uy = (t.x - s.x)*math.sin(theta) + (t.y - s.y)*math.cos(theta) + s.y
    u = Point(ux,uy)

    koch_curve(d-1,p1,s)
    print(s)
    koch_curve(d-1,s,u)
    print(u)
    koch_curve(d-1,u,t)
    print(t)
    koch_curve(d-1,t,p2)

    return None



print("input n:")
n = int(input())
print("koch curve points:")

p1 = Point(0,0)
p2 = Point(100,0)

print(p1)
koch_curve(n,p1,p2)
print(p2)
