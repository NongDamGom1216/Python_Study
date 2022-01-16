#매핑해준다
#A였던 것을 가공해서 B로 만든다
#데이터 갯수는 변하지 않는다. (filter 함수는 데이터 갯수가 변경됨)
#filter, map, sort 함수들의 공통점 => 함수를 인자로 받는다.

def total(s, b):
    return s + b
score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]
for s in map(total, score, bonus): #2개의 값을 받아서 더해서 출력
    print(s, end = ", ")