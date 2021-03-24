"""
Maximum Heap
最大ヒープ

データ構造を作成する上で、データの到着順ではなくデータがもつあるキーを基準にして
優先度順が高いものから取り出す優先度付きキューは、
二分ヒープ（完全二分木）を用いることにより比較的簡単に実装できる

最も大きい値が根になるような最大ヒープを作成する

キーを連続でinputされた時に作成された
Maxヒープをノード番号を１から順に出力する

"""

parent  = lambda data : int(data/2)
left  = lambda data : int(data*2)
right  = lambda data : int(data*2+1)

def maxHeapfify(input_data,i):
    pass        

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
    
    N = len(input_data)
    for i in reversed(range(1,N/2)):
        maxHeapfify(input_data,i)
