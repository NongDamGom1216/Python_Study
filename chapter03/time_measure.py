from time_util import get_measure_time

def work():
    for a in range(1000):
        print(a)

def work2(): #1에서 1000까지의 합을 구하는데 걸리는 시간 출력
    total = 0
    for a in range(1, 1001):
        total += a

def main():
    measure_time = get_measure_time(work)
    print(measure_time)

    measure_time = get_measure_time(work2)
    print(measure_time)

main()