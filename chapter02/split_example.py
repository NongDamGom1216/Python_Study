s ="._."
print(s.join("대한민국"))

#리스트를 하나의 문자열로
def main():
    names = ["히나나", "하지메", "시마린", "신학", "요이미야"]

    print(names)

    # names의 각 이름을 한 줄에 하나씩 출력하세요.
    print('\n'.join(names))

    # names의 각 일므을 ""에 구분하여 하나의 문자열로 만드세요.
    new_names = ', '.join(names)
    print(new_names)

main()