def insum(*ints): #튜플을 나타내는 가변인수, 값 여러개를 받을 수 있는 변수가 됨

    print(type(ints))
    print(ints)

    total = 0
    for num in ints:
        total += num
    
    return total

print(insum(1, 2, 3))
print(insum(5, 7, 9, 11, 13))
print(insum(8, 9, 6, 2, 9, 7, 5, 8))