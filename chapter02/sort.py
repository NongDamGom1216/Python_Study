score = [88, 95, 70, 100, 99]

score.sort() #오름차순
print(score)

score.reverse() #내림차순
print(score)

score.sort(reverse=True) #sort를 사용한 내림차순
print(score)

score = [88, 95, 70, 100, 99]
sorted_score = sorted(score, reverse=True) #원본은 유지하고 새로운 리스트로 초기화
print(score)
print(sorted_score)

#오름차순으로 정렬된 상태에서 max(), min() 함수를 사용하지 않고, 최소값, 최대값을 출력하는 법
def main():
    score = [88, 95, 70, 100, 99]
    score.sort() #오름차순
    print(f'최소값: {score[0]} 최대값: {score[-1]}') #score[len(score)-1]

main()

#대소문자 상관없이 정렬하는 법, sorted 사용하지 않고 원본은 유지하는 법(key = str.lower)
def main2():
    country = ["Korea", "japan", "CHINA", "america"]
    country.sort(key = str.lower) #key에 적용할 함수를 선택할 수 있다
    print(country)

main2()

#대소문자 상관없이 정렬하는 법, comprehension 사용
def main3():
    country = ["Korea", "japan", "CHINA", "america"]
    country = [i.lower() for i in country]
    country.sort()
    print(country)

main3()

#문자열의 길이가 긴 순으로 정렬
def main_sort():
    country = ["South Korea", "japan", "CHINA", "america"]
    country.sort(key=len, reverse=True)
    print(country)

main_sort()