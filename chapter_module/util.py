INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

print('util.py', __name__)
# __name__ : 모듈명을 저장하고 있는 변수
# 모듈로써 사용이 안되었으면 항상 main으로 나옴
#if __name__ == "__main__" :
# --> True면 실행 주체 파일이고, False면 모듈로 쓰이는 걸 나타낸다.

if __name__ == "__main__" :
    print("1inch = ", INCH)
    print("~10 = ", calcsum(10))
#APP.EX/menu.py에서 예시