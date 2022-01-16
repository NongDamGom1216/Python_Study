#range(시작, 끝[,증가값])
total = 0
for num in range(1, 101): #1 ~ 100, 마지막은 포함안됨
    total += num

print("total = ", total )

total = 0
for num in range(2, 101, 2): #2씩 증가하는 옵션 추가, 짝수의 합
    total += num

print("total = ", total )

total = 0
START = int(input("시작값: "))
END = int(input("끝값: "))

for num in range(START, END+1): # +1 하는거 주의해야한다.
    total += num
print("total = ", total )