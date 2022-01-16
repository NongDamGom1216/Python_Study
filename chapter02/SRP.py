#단일 책임 원칙(single responsibility principle)이란 모든 클래스는 하나의 책임만 가진다.
def printsum(n):
    total = 0
    for num in range(n+1): #계산도 하고
        total += num
    print("~", n, "=", total) #출력도 한다

    #이 함수는 단일 책임 원칙에 해당되지 않아 재사용하기 힘들다.