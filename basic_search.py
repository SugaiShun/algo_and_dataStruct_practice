"""
Basic Search Program

Linear Search
Binary Search
Hash Search
"""

def LinearSearch(inputs,key):
    """
    LineraSearch(inputs,key)
    ipnuts:list
    key:search key
    """
    inputs.append(key)
    index=0
    while inputs[index]!=key:
        index+=1
    if (index+1)==len(inputs):
        return None

    return index

def BinarySearch(inputs,key):
    """
    BinarySearch(inputs,key)
    ipnuts:list
    key:search key
    """
    left = 0
    right = len(inputs)
    while left<right:
        mid = int((left + right)/2)
        if inputs[mid] == key:
            return mid
        elif inputs[mid] < key:
            left = mid + 1
        else:
            right = mid

HASHSIZE = 10
H = [None]*10
def _h1(key):
    return key%HASHSIZE
def _h2(key):
    return 1+key%(HASHSIZE-1)
def HashInsert(inputs):
    """
    HashInsert(inputs) Open Address 
    ipnuts:list
    """
    for key in inputs:
        i = 0
        while(1):
            h = (_h1(key) + i * _h2(key) ) % HASHSIZE
            if H[h] == None:
                H[h] = key
                break
            i+=1

def HashSearch(key):
    """
    HashSearch(key) Open Address
    key:int
    """
    i = 0
    while(1):
        h = (_h1(key) + i * _h2(key) ) % HASHSIZE
        if H[h] == key:
            return h
        elif H[h] == None:
            return None
        i+=1

if __name__ == "__main__":
    '''
    数値を標準入力で連続で受け取るメインプログラム
    '''
    print("start first inputs. if you completed inputs, you type \"end\".")

    input_data1 = []
    input_data2 = []
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            input_data1.append(int(tmp))
    print("start second inputs. if you completed inputs, you type \"end\".")
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            input_data2.append(int(tmp))

    HashInsert(input_data1)

    cnt = 0
    for key in input_data2:
        # if LinearSearch(input_data1,key)!=None:
        #     cnt+=1

        # input_data1.sort()
        # if BinarySearch(input_data1,key)!=None:
        #     cnt+=1

        index = HashSearch(key)
        if index!=None:
            print(index)
            cnt+=1

    print(str(cnt))
