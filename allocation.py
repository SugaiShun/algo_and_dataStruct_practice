"""
Allocation Program
重さがそれぞれw_i(w1,w2,...wn)のn個の荷物が
ベルトコンベアから順番に送られてくる.
これらの荷物をk個のトラックに積み込む.
トラックには最大積載量Pが設けられており、
最悪０個のトラックがあっても構わない.

w_n,n,kが与えられたとき,
全ての荷物を積むのに最小なPを求めよ.

入力例.
n=5
k=3
w1=8
w2=1
w3=7
w4=3
w5=9
回答.
P=10

条件：
1 ≦ n ≦ 100,000
1 ≦ k ≦ 100,000
1 ≦ w ≦ 100,000
1secで処理すること
"""
import basic_search as search


def check(weights,k,p):
    n = len(input_weights)
    i = 0
    for j in range(k):
        s = 0
        while s + input_weights[i] <= p:
            s += input_weights[i]
            i += 1
            if i == n:
                return n
    return i


print("k=",end="")
k = int(input())
print("Please input weights. if you completed inputs, you type \"end\".")

input_weights = []
while(1):
    tmp = input()
    if tmp == "end":
        break
    else:
        input_weights.append(int(tmp))

right = 100000
left = 0
n = len(input_weights)
while (right-left) > 1:
    p = int((left + right)/2)
    if check(input_weights,k,p) >= n:
        right = p
    else:
        left = p

print("p="+str(right))


