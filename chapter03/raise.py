def calcsum(n):
    if n < 0 :
        raise ValueError #개발자에 의해 임의로 예외를 발생시킴

    total = 0
    for i in range(n+1):
        total += i
    return total
try:
    print("~10 =", calcsum(10))
#    print("~-5 =", calcsum(-5))
except ValueError:
    print('입력값이 잘못되었습니다.')


print("-"*100)

#assert 단정문, 반드시 이 조건이어야 한다.
try:
    score = 128
    assert score <= 100, "점수는 100 이하여야 합니다."
    print(score)
except Exception as e:
    print(e)
    