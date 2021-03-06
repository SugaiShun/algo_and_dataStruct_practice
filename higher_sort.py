"""
Sort Problem
1. Merge Sort -> mergeSort(data:list,left-index:int,right-index:int)
2. Partition
3. Quick Sort
4. Counting Sort
"""

def merge(data,left,right):
    mid = int( (left+right) / 2 )
    n1 = mid - left
    n2 = right - mid
    leftData = [ data[i+left] for i in range(n1) ]
    rightData = [ data[i+mid] for i in range(n2) ]
    i = 0
    j = 0
    leftData.append(float("inf"))
    rightData.append(float("inf"))
    for k in range(left,right):
        if leftData[i] <= rightData[j]:
            data[k] = leftData[i]
            i += 1
        else:
            data[k] = rightData[j]
            j += 1


def mergeSort(data,left,right):
    if left + 1 < right:
        mid = int( (left+right) / 2 )
        mergeSort(data,left,mid)
        mergeSort(data,mid,right)
        merge(data,left,right)

if __name__ == "__main__":
    print("Input Sequence A. if you completed inputs, you type \"end\".")
    input_data = []
    while True:
        tmp=input()
        if tmp == "end":
            break
        else:
            input_data.append(int(tmp))

    mergeSort(input_data,0,len(input_data))

    print(input_data)
