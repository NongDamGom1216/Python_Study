for y in range(9, 0, -1): #시작하는 값 9, 끝나는 값 0, 증감값은 -1
    for x in range(y):
        print('*', end='')
    print()

print()

#이중루프처럼 안보이지만 이중루프다
for y in range(1, 10):
    print('*'*y)