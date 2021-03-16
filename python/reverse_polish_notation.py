"""
逆ポーランド記法の数式計算
（１＋２）＊（５＋４）といった計算式は、
逆ポーランド記法では1 2 + 5 4 + *といった表記がされる
（これによりカッコ等の記載がなくて済むメリットがある）
"""

from basic_dataStruct import stack

def reverse_polish_notation(input_string):
    input_data = input_string.split()
    
    stack_list = stack()
    for data in input_data:
        if data == "+":
            if stack_list.size() < 2:
                print("formula error.")
            else:
                value1 = stack_list.pop()
                value2 = stack_list.pop()
                input_value = value1 + value2
                stack_list.push(input_value)
        elif data == "-":
            if stack_list.size() < 2:
                print("formula error.")
            else:
                value1 = stack_list.pop()
                value2 = stack_list.pop()
                input_value = value1 - value2
                stack_list.push(input_value)
        elif data == "*":
            if stack_list.size() < 2:
                print("formula error.")
            else:
                value1 = stack_list.pop()
                value2 = stack_list.pop()
                input_value = value1 * value2
                stack_list.push(input_value)
        elif data == "/":
            if stack_list.size() < 2:
                print("formula error.")
            else:
                value1 = stack_list.pop()
                value2 = stack_list.pop()
                input_value = value1 / value2
                stack_list.push(input_value)
        else:
            stack_list.push(int(data))
    
    return stack_list.pop()

if __name__ == "__main__":
    '''
    １行のみを受け取る
    '''
    print("start input data. ")

    input_string = input()
    output = reverse_polish_notation(input_string)

    print(output)    
