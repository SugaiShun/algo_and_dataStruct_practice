"""
Sort Problem
1. Merge Sort -> mergeSort(data:list,left-index:int,right-index:int)
2. Partition -> partition(data:list,left-index:int,right-index:int)
3. Quick Sort -> quickSort(data:list,left-index:int,right-index:int)
4. Counting Sort -> countingSort(data:list, k:int):return sorted list
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

def partition(data,p,r):
    x = data[r]
    i = p - 1
    for j in range(p,r):
        if data[j] <= x:
            i += 1
            t = data[i]
            data[i] = data[j]
            data[j] = t
    t = data[i+1]
    data[i+1] = data[r]
    data[r] = t
    return i+1

def quickSort(data,p,r):
    if p < r:
        q = partition(data,p,r)
        quickSort(data,p,q-1)
        quickSort(data,q+1,r)

def countingSort(data,k):
    C = [0]*k
    B = [0]*(len(data)+1)

    data.insert(0,0)

    for i in range(1,len(data)):
        C[data[i]]+=1
    for j in range(1,k):
        C[j] = C[j] + C[j-1]
    for i in reversed(range(1,len(data))):
        B[C[data[i]]] = data[i]
        C[data[i]] -= 1
    
    data.pop(0)
    B.pop(0)

    return B

if __name__ == "__main__":
    print("Input Sequence A. if you completed inputs, you type \"end\".")
    input_data = []
    while True:
        tmp=input()
        if tmp == "end":
            break
        else:
            input_data.append(int(tmp))

    # mergeSort(input_data,0,len(input_data))
    # print(input_data)
    # i = partition(input_data,0,len(input_data)-1)
    # print(input_data)
    # print(i)
    # quickSort(input_data,0,len(input_data)-1)
    # print(input_data)
    sorted_data = countingSort(input_data,100)
    print(sorted_data)

