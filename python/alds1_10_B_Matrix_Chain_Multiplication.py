"""
Matrix Chain Multiplication
連鎖行列積

ある計算式に対して、一度計算した結果をメモリに記憶しておき、同じ計算を繰り返し
行う無駄を避けつつ、それらを再利用することによる効率化
その手法の１つが動的計画法である

n個の行列の連鎖　M1,M2,M3,...,Mnが与えられたとき、
スカラー乗算の回数が最小になるように積M1M2M3..Mnの計算順序を決定する問題を
連鎖行列積問題という

n個の行列について、行列Miの次元が与えられたとき、
積M1M2M3...Mnの計算に必要なスカラー乗算の最小の回数を求める

"""

def matrixChainMultiplication(p):

    n = len(p)
    m = [ [0]*n for i in range(n) ]
    for l in range(2,n):
        # l : 何個の行列の組み合わせをみるか

        for i in range(1,n-l+1):
            # i : 組み合わせの始まりの行列
            # j : 組み合わせの終わりの行列
            j = i + l - 1
            for k in range(i, j):
                # k : iとjの行列
                new_m = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if new_m < m[i][j] or m[i][j]==0 : m[i][j] = new_m

    return m[1][n-1]

if __name__ == "__main__":

    input_datas = []
    input_datas.append("30 35")
    input_datas.append("35 15")
    input_datas.append("15 5")
    input_datas.append("5 10")
    input_datas.append("10 20")
    input_datas.append("20 25")

    p = []
    for i in range(len(input_datas)):
        data = input_datas[i].split()
        if i == 0: p.append(int(data[0]))
        p.append(int(data[1]))
    
    output = matrixChainMultiplication(p)
    print("output:{}".format(output))
