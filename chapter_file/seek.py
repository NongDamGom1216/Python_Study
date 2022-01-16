#단위가 바이트, 한글인 경우에 글자 하나가 3바이트
f = open("live.txt", "rt", encoding="utf-8")

f.seek(13, 0) #12 바이트일 경우 문자 중간 위치에 있어서 예외 발생
text = f.read()
f.close()

print(text)