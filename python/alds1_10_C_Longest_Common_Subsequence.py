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


def lcs_original(X,Y):
    global cnt_original
    rslt = []
    
    size_X = len(X)
    size_Y = len(Y)
    size_XY = size_X if size_X > size_Y else size_Y

    j = 0
    for i in range(size_XY):

        m_max = i+1 if i+1 <size_X else size_X
        for m in range(j,m_max):
            n_max = i+1 if i+1 < size_Y else size_Y
            for n in range(j,n_max):
                cnt_original+=1
                if X[m] == Y[n]:
                    rslt.append(X[m])
                    j = i+1

    return rslt

if __name__ == "__main__":

    input_X = ['a','b','c','b','d','a','b']
    input_Y = ['b','d','c','a','b','a']

    # input_X = ['a','b','c']
    # input_Y = ['b','d']

    output_Z = lcs_original(input_X,input_Y)

    print("output:{}".format(output_Z))
    print("caluculation:{}".format(cnt_original))

    output_Z = lcs_ans(input_X,input_Y)
    print("output:{}".format(output_Z))
    print("caluculation:{}".format(cnt_ans))
