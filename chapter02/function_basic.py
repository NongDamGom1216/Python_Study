def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num
    return total

print("1부터 10의 합", calcsum(10))

def calcrange(begin, end, step): #step을 스킵하면 증감은 1
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

print("3 ~ 7의 합은 ", calcrange(3, 7, 1))
print("2 ~ 10의 짝수합은 ", calcrange(2, 10, 2))

#디폴트 값 적용하는 법
def calcrange(begin, end = 1, step = 1): #step을 스킵하는 방법, 스킵할 경우 1이 된다.
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

print("3 ~ 7의 합은 ", calcrange(3, 7))
print("0 ~ 1의 합은 ", calcrange(0))