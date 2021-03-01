"""
Exhausetive Search
再帰関数を用いた全探索問題

ある数列Aに対して整数mが与えられたとき、
数列Aの中の組み合わせで整数mを作ることができるかを判定する
"""


input_data = []
n = 0
def solve(i,m):
    rslt = False

    if m == 0:
        return True
    elif i >= n:
        return False
    
    rslt = solve(i+1,m) or solve(i+1,m-input_data[i])
    return rslt


print("Input Sequence A. if you completed inputs, you type \"end\".")
while True:
    tmp=input()
    if tmp == "end":
        break
    else:
        input_data.append(int(tmp))

n = len(input_data)

print("Input M.")
M = input()
diagnosis = solve(0,int(M))
print(diagnosis)