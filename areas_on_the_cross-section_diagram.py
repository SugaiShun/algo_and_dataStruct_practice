"""
Areas on the Cross Section Diagram
地域の模式断面図が与えれらたとき、
雨が降り続けた際の洪水状況をシミュレートする

入力例.
\\\////\/\_/
この入力を受け取る時、断面図は以下のようになる
       /\/\_/
 \    /
  \  /
   \/
貯水量は9+1+3=13となる
"""
from basic_dataStruct import stack

def diagram_simulation(input_data):

    s1 = stack()
    s2 = stack()
    itr = 0
    all_capacity = 0
    for cross_sec_info in input_data:
        if cross_sec_info == "\\":
            s1.push(itr)
        elif cross_sec_info == "/" and s1.size() > 0:
            pair_position = s1.pop()
            capacity = itr - pair_position
            all_capacity += capacity

            while s2.size()>0 and s2.top()[0] > pair_position:
                capacity += s2.pop()[1]
            s2.push((pair_position,capacity))
            
        itr += 1

    return all_capacity,s2

if __name__ == "__main__":
    print("input the cross-section data")

    input_data = input()
    sum_capa,sections = diagram_simulation(input_data)

    print("sum capacity:"+str(sum_capa))
    cnt = 1
    while sections.size()>0:
        print("section"+str(cnt)+":"+str(sections.pop()[1]))
        cnt+=1
