#판별하고자 하는 함수는 True/False
def flunk(s):
    return s < 60
score = [ 45, 89, 72, 53, 94 ]
for s in filter(flunk, score):
    print(s)

print('-'*20)

#90점 이상의 고득점
def high_score(s):
    return s >= 90

result = list(filter(high_score, score))
print(result)

print('-'*20)

#filter 함수를 사용하지 않고 60점 미만 성적 찾기
result = []
for s in score:
    if s < 60:
        result.append(s)
        
print(result)