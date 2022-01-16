#리스트에 들어있는 성적 데이터의 최솟값을 구하시오.

scores = [34, 78, 90, 35, 100, 88, 10]

min_score = 101 #scores[0]도 실행은 된다.
total = 0

for x in scores: #문법 알아두기
    if (min_score > x):
        min_score = x

print('최솟값: ', min_score)
