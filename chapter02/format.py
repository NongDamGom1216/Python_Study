#예전 기법
mont = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." %(mont, day, anni))

#요즘 기법 #f-string
s = '일'
print(f'나는 하고 싶은 {s}을 하면서 살고싶다.')

hour = 7
print(f'나는 {hour}시에 밥 먹을거야')


#{변수:숫자}
#여기서 숫자는 폭의 길이를 말하는 것

# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
# f-string 가운데 정렬 
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
# f-string 오른쪽 정렬 
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

f1 = 12.3456
result1 = f'{f1:.2f}' # 소수점 셋째자리에서 반올림
print(result1)

year = 2022
month = 1
day = 1

#f를 맨 앞에 쓰는 걸 기억해야한다
# 작성일 : 2022-01-01
print(f'작성일: {year}-{month}-{day}')
print(f'작성일: {year}-{month:2}-{day:2}') #2자리씩
print(f'작성일: {year}-{month:02}-{day:02}') #0을 붙여서 하면 제대로 출력된다