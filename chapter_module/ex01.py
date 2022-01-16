import util

print("1inch = ", util.INCH)
print("~10 = ", util.calcsum(10))

print('ex01.py', __name__)

# __name__ : 모듈명을 저장하고 있는 변수
# 모듈로써 사용이 안되었으면 항상 main으로 나옴
#if __name__ == "__main__" :
# --> True면 실행 주체 파일이고, False면 모듈로 쓰이는 걸 나타낸다.