def main():

    s = "python programming"

    print(len(s))
    print(s.find('o')) #이건 많이 쓰임
    print(s.rfind('o'))
    print(s.index('r'))
    print(s.count('n'))

main()

#.find(str): str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
#.rfind(str): 뒤에서 str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
#.index(str): find()와 동일, 없으면 예외 발생
#.count(str): str 문자열이 몇번 등장하는지 리턴

names = ["시부야린", "시마린", "이치카와히나나", "샤오린", "린코"]
search_name = input("검색이름 : ")
#검색 이름이 포함된 모든 이름을 출력

for name in names:
    if name.find(search_name) > -1 : #인덱스가 반환되기 때문에!!!
        print(name)
    

for name in names:
    if search_name in name: #결과가 같다.
        print(name)
