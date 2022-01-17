# 지역 함수, 함수 안에 함수를 정의한다.

def calcsum(n):
    def add(a, b):
        return a + b
    total = 0
    for i in range(n+1):
        total = add(total, i)
    return total

print("~ 10 = ", calcsum(10))

print()
print('-'*50)

# 지역 함수 예제, 중요!
def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Morning") #message = "Good Morning"
#여기서 메모리에 print("Good Morning" + ", " + "name")이 들어있음
kohello = makeHello("안녕하세요")

enghello("Mr Kim") #name으로 전달됨
kohello("홍길동")

print()
print('-'*50)
print()
print()
print()

import time

def inner():
    print("결과를 출력합니다.")

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

def elapse(func): #함수의 실행 시간 측정 및 시간 출력 함수
    def measure():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} 함수 실행 시간: {end-start}')
    return measure

@outer # inner = outer(inner)를 함수뒤에 선언한 것과 같음
def inner():
    print("데코레이션 결과")

@outer
@elapse
 # time_measure = outer(elapse(time_measure))
def time_measure():
    print("시간 측정")

inner()
time_measure()