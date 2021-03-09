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
import random
import datetime
import time

def check(weights,k,p):
    n = len(weights)
    i = 0
    for j in range(k):
        s = 0
        while s + weights[i] <= p:
            s += weights[i]
            i += 1
            if i == n:
                return n
    return i

if __name__ == "__main__":
    max_v = 100
    n = 100000
    k = 100

    # 重複なしの整数データ
    input_data = [ random.randint(0,max_v) for i in range(n) ]
    # random.sample(range(max_v), k=n)

    print("start time: {}".format(datetime.datetime.now()))
    time1 = time.perf_counter()

    right = 100000*100000
    left = 0
    n = len(input_data)
    while (right-left) > 1:
        p = int((left + right)/2)
        if check(input_data,k,p) >= n:
            right = p
        else:
            left = p
    time2 = time.perf_counter()
    print("p="+str(right))
    print("elapsed time: {} [ms]".format((time2-time1)*1000))

    



