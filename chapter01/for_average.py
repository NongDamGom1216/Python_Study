#for a in range(10) 이면 0부터 9이다.

for x in range(1, 51): #1부터 50
    if (x % 10) == 0:
        print('+', end = '')
    else:
        print('-', end = '')

print('')

#리스트에 들어있는 성적 데이터의 평균을 구하시오. for문 사용

scores = [34, 78, 90, 35, 100, 88]

average = 0
total = 0

length = len(scores) #for 문 안에서 count += 1을 추가해서 count 값을 나중에 나눠도 됨

for x in scores: #문법 알아두기
    total += x

average = total / length

print('평균: ', round(average, 2)) # 소수 둘째자리까지 출력

#continue 연습

scores = [34, 78, 90, 35, 100, 120, 88]
total = 0

for score in scores:
    if (score < 0) or (score > 100):
        continue
    total += score

average = total / length

print('평균: ', round(average, 2)) # 소수 둘째자리까지 출력