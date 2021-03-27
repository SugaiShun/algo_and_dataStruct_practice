"""
Fibonacci Number
フィボナッチ数列

ある計算式に対して、一度計算した結果をメモリに記憶しておき、同じ計算を繰り返し
行う無駄を避けつつ、それらを再利用することによる効率化
その手法の１つが動的計画法である

nを入力して、フィナッチ数列を出力する

"""

f_cnt = 0
f_memory = 0

def fibonacci(n:int):
    global f_cnt

    if n == 0 or n == 1:
        f_cnt += 1
        f_memory[n-1] = 1
        return 1
    else:

        if f_memory[n-1] == 0:
            f_cnt += 1
            f_memory[n-1] = fibonacci(n-1) + fibonacci(n-2)

        return f_memory[n-1]

if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))
    n  = 10
    f_memory = [0]*n
    p = fibonacci(n)
    print("output:{}".format(p))
    print("calculation:{}".format(f_cnt))

