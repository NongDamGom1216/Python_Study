#열거하다
#번호를 주어 튜플로 만들어준다.
#리스트에서 인덱스 정보가 필요할 때 사용한다.
race = ['저그', '테란', '프로토스']
print(list(enumerate(race)))

score = [88, 95, 70, 100, 99]
for no, s in enumerate(score, 1): #1을 배정했기 때문에 1부터 시작한다.
    print(str(no) + "번 학생의 성적 : ", s)