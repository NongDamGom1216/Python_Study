salerate = 0.9

def kim():
    print("오늘의 할인율: ", salerate)

    

def lee():
    price = 1000
    print("가격 : ", price * salerate)

kim()
salerate = 1.1
lee()

#읽기할 때 -> 스택(지역변수공간)에서 먼저 확인하고 전역공간으로
#함수 내에서의 쓰기 작업은 스택(지역변수공간)에서 이루어짐


#함수 내에서 전역 변수를 업데이트하고 싶을 때
price = 1000
def sale():
    global price
    price = 500
sale()
print(price)