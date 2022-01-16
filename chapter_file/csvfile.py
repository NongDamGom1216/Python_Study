#텍스트로 되어있는 data.txt 파일을 읽어서 리스트의 정수로 복원

def main():
    try:
        with open('data.txt', 'rt' ) as file:
            content = file.read()
            print(content)

            # ,를 기준으로 토크나이징 해줘야함 -> split
            datas = content.split(',')
            print(datas)

            #문자열을 정수로 바꿔준다.
            datas = list(map(int, datas))
            print(datas)

    except Exception as e:
        print(e)
    
main()