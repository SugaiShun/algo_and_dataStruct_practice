"""
Round Robin Scheduling

名前name(i)と必要な処理時間time(i)をもつN個プロセスが順番に
一列に並んでいる時、CPUは各プロセスを最大q[ms]だけ処理を実行する.
（このときの最大q[ms]をクオンタムと呼ぶ）
それでもプロセスが完了しない時、そのプロセスは列の最後尾に回し、
CPUは次のプロセスが割り当てられる.
"""
from basic_dataStruct import queue_likeC


queue = queue_likeC(50)

def round_robin_scheduling(quantum=500):

    while(queue.head!=queue.tail):
        process_name,process_time = queue.dequeue()
        if process_time > quantum:
            remainer_time = process_time - quantum
            queue.enqueue((process_name,remainer_time))
            process_time = quantum
        print(process_name+" processed "+str(process_time)+"ms")

if __name__ == "__main__":
    '''
    数値を標準入力で連続で受け取るメインプログラム
    '''
    print("start input data. if you completed input, you type \"end\".")

    input_data = []
    cnt = 0
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            queue.enqueue(("id"+str(cnt),int(tmp)))
        cnt+=1
    
    round_robin_scheduling()

