"""
Priority Queue
優先度付きキュー

データ構造を作成する上で、データの到着順ではなくデータがもつあるキーを基準にして
優先度順が高いものから取り出す優先度付きキューは、
二分ヒープ（完全二分木）を用いることにより比較的簡単に実装できる

優先度付きキューへの挿入
最大値の取り出し
を実装する

"""

parent  = lambda data : int(data/2)
left  = lambda data : int(data*2)
right  = lambda data : int(data*2+1)


def extract(input_data):

    max_key = input_data[0]
    input_data[0] = input_data.pop(-1)
 
    input_data.insert(0,None)
    maxHeapfify(input_data,1)
    input_data.pop(0)
    
    return max_key

def insert(input_data,key):

    input_data.insert(0,None)
    input_data.append(key)

    H = len(input_data)-1
    p_id = parent(H)
    while p_id > 0 and input_data[p_id] < key:
        tmp = input_data[p_id]
        input_data[p_id] = key
        input_data[H] = tmp

        H = p_id
        p_id = parent(H)

    input_data.pop(0)

def maxHeapfify(input_data,i):
    l = left(i)
    r = right(i)

    N = len(input_data)
    large_i = i
    if l < N and input_data[l] > input_data[large_i]: large_i = l
    if r < N and input_data[r] > input_data[large_i] : large_i = r

    if large_i != i:
        tmp = input_data[large_i]
        input_data[large_i] = input_data[i]
        input_data[i] = tmp

        maxHeapfify(input_data,large_i)

if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append(4)
    input_data.append(1)
    input_data.append(3)
    input_data.append(2)
    input_data.append(16)
    input_data.append(9)
    input_data.append(10)
    input_data.append(14)
    input_data.append(8)
    input_data.append(7)
    
    input_data.insert(0,None)
    N = len(input_data)
    H = int(N/2)
    for i in reversed(range(1,H)):
        maxHeapfify(input_data,i)
    input_data.pop(0)

    print(input_data)

    insert(input_data,20)

    print(input_data)

    max_key = extract(input_data)

    print(max_key)
    print(input_data)
    
