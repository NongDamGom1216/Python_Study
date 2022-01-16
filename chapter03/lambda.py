#한 줄로 정의되는 함수의 축약 표현(한 줄로 구현 가능한 함수를 매개변수로 전달할 때 사용)
#변수에 대입해서 사용, 함수의 이름이 없음, 아주 간단한 식

score = [ 45, 89, 72, 53, 94 ]
for s in filter(lambda x: x < 60, score):
    print(s, end = ', ')

print()
print('-'*20)

#람다 함수로 90점 이상 출력하기
score = [ 45, 89, 72, 53, 94 ]
high =  list(filter(lambda x: x >= 90, score))
print(high)

print('-'*20)

#람다 함수로 데이터를 반으로 나누기(매핑)
score = [45, 89, 72, 53, 94]
result =  list(map(lambda x: x / 2, score))
print(result)