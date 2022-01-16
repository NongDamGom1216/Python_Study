try:
    f = open("live.txt", "rt", encoding="utf-8")
    text = f.read()

    lines = text.split('\n') #라인별로 끊어서 리스트에 넣는다.
    #print(lines)

    for ix, line in enumerate(lines, 1): #1부터 넘버링
        print(f'{ix} : {line}')

    #print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

print("-"*100)


#파일 넘버링 2번째 방법
f = open("live.txt", "rt", encoding="utf-8")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break #파일의 끝까지 읽으면 None 리턴
    text += str(line) + " : " + row
    line += 1

f.close()
print(text)

print("-"*100)

#파일 읽기 2번째 방법
f = open("live.txt", "rt", encoding="utf-8")
rows = f.readlines()
print(rows) #개행 문자("\n")가 포함되어 있다.
for row in rows:
    print(row, end="") #개행 문자가 포함되어 있기 때문에 end=""를 해줘야한다.
f.close()

print()
print("-"*100)

#파일 읽기 3번째 방법
f = open("live.txt", "rt", encoding="utf-8")
for line in f:
    print(line, end="")
f.close()