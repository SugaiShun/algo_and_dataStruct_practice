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
    
    cnt = 0
    for key in input_data2:
        # if LinearSearch(input_data1,key)!=None:
        #     cnt+=1

        input_data1.sort()
        if BinarySearch(input_data1,key)!=None:
            cnt+=1

    print(str(cnt))
