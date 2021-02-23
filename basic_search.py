"""
Basic Search Program

Linear Search
Binary Search
Hash Search
"""

def _LinearSearch(inputs,key):
    inputs.append(key)
    index=0
    while inputs[index]!=key:
        index+=1
    if (index+1)==len(inputs):
        return None

    return index

def LinearSearch(input1,input2):
    
    cnt=0
    for key in input2:
        if _LinearSearch(input1,key)!=None:
            cnt+=1

    return cnt


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
    
    output = LinearSearch(input_data1,input_data2)

    print(output)    
