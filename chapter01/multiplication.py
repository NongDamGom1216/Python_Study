#구구단 출력

number = int(input("구구단 숫자 입력: "))
result = 0

for i in range(1, 10):
    result = number * i
    print(number, 'x', i, '=', result)


#강사님 예제 #이중루프

dan = 3

for dan in range(2, 10):
    print(dan, '단')
    for hang in range(1, 10):
        print(dan, 'x', hang, '=', dan * hang)
    print() #줄만 바꿔줌