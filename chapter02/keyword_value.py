#어렵다!
#키워드 가변 인수
def calcstep(**args): #키워드 가변 인수는 2개
    print(type(args)) #dictionary
    print(args)

    func_begin = args['begin']
    func_end = args['end']
    func_step = args.get('step', 1) #()이다.

    total = 0
    for num in range(func_begin, func_end +1, func_step):
        total += num
    return total

print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3, test=1000))
print("3 ~ 5 =", calcstep(begin=3, end=5)) #get으로 디폴트값 지정해주면 생략 가능

#가변 변수, 키워드 가변 변수 동시 사용
def calcscore(name, *score, **option): #함수를 정의할 때 *를 붙이면 튜플로, **를 붙이면 사전으로
    print(name)
    print(score)
    print(option)

    total = 0
    for s in score:
        total += s

    print("총점 :", total)
    if(option.get('avg') == True):
        print("평균 :", total/len(score))
    print()

#calcscore("히나나", 88, 99, 77, avg=True)
#calcscore("노엘", 99, 88, 95, 85, avg=False)
#calcscore("텐카", 59, 68, 35, 45, 100, avg=True)

hinana_score = [88, 99, 77]
noel_score = [99, 88, 95, 85]
tenka_score = [59, 68, 35, 45, 100]

option = {
    'avg' : True,
    'total' : True,
}
#함수를 호출할 때 *를 붙이면 펼쳐라, **를 붙이면 사전을 펼쳐서 키워드 인수로 전달해라
calcscore("히나나", *hinana_score, **option)
calcscore("노엘", *noel_score, avg=True)
calcscore("텐카", *tenka_score, avg=False)
