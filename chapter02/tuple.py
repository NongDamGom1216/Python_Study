#튜플 응용법
names = "이순신", "김유신", "강감찬"
lee, kim, kang = names #튜플이다, 갯수 맞춰야한다
print(lee)
print(kim)
print(kang)

#튜플은 변수 초기화에 쓰인다.
a, b = 12, 34
print(a, b)
a, b = b, a
print(a, b)

import time
def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print(f"지금은 {result[0]}시 {result[1]}분 입니다.")

hour, minute = gettime()
print("지금은 %d시 %d분 입니다."%(hour, minute))


scores = [
    ("히나나", 90),
    ("가은", 80),
    ("노엘", 79),
]

for score in scores:
    print(f'학생명: {score[0]}, 성적: {score[1]}')

print()

for name, score in scores:
    print(f'학생명: {name}, 성적: {score}')