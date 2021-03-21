"""
Maximum Profit
FX取引において、時刻tにおける価格R[t](t=0,1,2,...,n-1)が入力として与えられる時、
価格R[j] - R[i]の最大値を求めよ
ここでjとiは（j>i）の関係を満たすものとする

発展：nを1<n<200,000の範囲とし、処理時間を1sec以内とするようにせよ
"""

def problem_2_5_better(input_data):
    cnt = 0
    profit = input_data[1] - input_data[0]
    min_input = input_data[0]
    for j in range(1,len(input_data)):
        tmp_profit = input_data[j] - min_input
        if profit < tmp_profit: profit = tmp_profit
        if min_input > input_data[j]: min_input = input_data[j]

    return profit

def problem_2_5_classic(input_data):
    cnt = 0
    profit = input_data[1] - input_data[0]
    for r_i in input_data:
        input_data_comp = input_data[(cnt+1):]
        for r_j in input_data_comp:
            tmp_profit = r_j - r_i
            if tmp_profit > profit:
                profit = tmp_profit
        cnt+=1
        if cnt==len(input_data):
            break

    return profit

if __name__ == "__main__":
    '''
    数値を標準入力で連続で受け取るメインプログラム
    '''
    print("start input data. if you completed input, you type \"end\".")

    input_data = []
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            input_data.append(int(tmp))
    
    # output = problem_2_5_classic(input_data)
    output = problem_2_5_better(input_data)

    print(output)    
