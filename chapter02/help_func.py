def calcsum(n):
    """1~n까지의 합계를 구해 리턴한다."""
    total = 0
    for i in range(n+1):
        total += i
    
    return total

help(calcsum)

#함수의 도움말을 나타낸다.
#help(함수명)으로 호출할 시 """ """ 안의 문장이 출력된다.