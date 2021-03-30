"""
Longest Common Subsequence
最長共通部分列

ある計算式に対して、一度計算した結果をメモリに記憶しておき、同じ計算を繰り返し
行う無駄を避けつつ、それらを再利用することによる効率化
その手法の１つが動的計画法である

２つの列X＝{x1,x2,...,xm}, Y={y1,y2,...,yn}が与えられたとき、
最長共通部分列Zを求める
例.)
X={a,b,c,b,d,a,b},Y={b,d,c,a,b,a}のとき、
Z={b,c,b,a}が最長共通部分列となる

"""

cnt_original = 0
cnt_ans = 0


def lcs_ans(X,Y):
    global cnt_ans
    
    X.insert(0,"")
    Y.insert(0,"")

    size_X = len(X)
    size_Y = len(Y)
    maxl = '0'

    rslt = []
    [ rslt.append(['0']*size_Y) for j in range(size_X) ]

    for i in range(1,size_X):
        for j in range(1,size_Y):
            # if X[i] == Y[j]:
            #     rslt[i][j] = rslt[i-1][j-1] + 1
            # elif rslt[i-1][j] >= rslt[i][j-1]:
            #     rslt[i][j] = rslt[i-1][j]
            # else:
            #     rslt[i][j] = rslt[i][j-1]

            # if rslt[i][j] > maxl: maxl = rslt[i][j] 

            if X[i] == Y[j]:
                rslt[i][j] = rslt[i-1][j-1] + X[i]
            elif len(rslt[i-1][j]) >= len(rslt[i][j-1]):
                rslt[i][j] = rslt[i-1][j]
            else:
                rslt[i][j] = rslt[i][j-1]

            if len(rslt[i][j]) > len(maxl): maxl = rslt[i][j]
            

            cnt_ans+=1
    
    return maxl[1:]

if __name__ == "__main__":

    # input_X = ['a','b','c','b','d','a','b']
    # input_Y = ['b','d','c','a','b','a']

    input_X = ['c','b','a','d']
    input_Y = ['b','d','c']

    # input_X = ['a','b','c']
    # input_Y = ['b','d']

    output_Z = lcs_ans(input_X,input_Y)
    print("output:{}".format(output_Z))
    print("caluculation:{}".format(cnt_ans))
