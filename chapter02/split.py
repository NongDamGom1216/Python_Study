#토크나이징을 하여 리스트로 만드는 작업
#split()안에 구분자를 지정해서 작업
s = "짜장 짬뽕 탕수육"
print(s.split()) #공백을 이용하여 구분

s2 = "서울->대전->대구->부산"
cities = s2.split("->") #화살표를 이용하여 구분
print(cities)

for city in cities:
    print(city)


def main():

    trabler = """
    강나루 거너서 밀밭 길을
    구름에 달 가듯이 가는 나그네
    """
    poet = trabler.splitlines() #\n
    print(poet)
    for line in poet:
        print(line)

main()
