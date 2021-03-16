"""
Random Input Program
"""
import random
import datetime
import time


def solver(input_data):
    """
    dummy program
    """
    for data in input_data:
        data2 = data + data


if __name__ == "__main__":
    max_v = 100000
    n = 100000
    # 重複ありの整数データ
    input_data_v1 = [ random.randint(0,max_v) for i in range(n) ]
    # 重複なしの整数データ
    input_data_v2 = random.sample(range(max_v), k=n)

    print("start time: {}".format(datetime.datetime.now()))
    time1 = time.perf_counter()
    solver(input_data_v1)
    solver(input_data_v2)
    time2 = time.perf_counter()

    print("elapsed time: {} [ms]".format((time2-time1)))

    



