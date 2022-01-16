# 키보드로 성적을 입력, 그 구간에 따라 학점 출력

score = int(input('점수를 입력: '))
grade = None

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score <= 89:
    grade = 'B'
elif score >= 70 and score <= 79:
    grade = 'C'
elif score >= 60 and score <= 69:
    grade = 'D'
else:
    grade = 'F'

print(score, '점은', grade, '학점입니다.')