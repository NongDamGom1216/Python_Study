def save(filename, content):
    with open(filename, 'wt', encoding="utf-8") as file:
        file.write(content)

def main():
    datas = [12, 34, 56, 78, 90]

    #리스트의 내용을 data.txt 파일로 저장하세요.
    #12,34,56,78,90 (문자열)

    #첫 번째 방법 : comprehension 사용해서 숫자 데이터를 문자열로 변환하기
    #content = [str(n) for n in datas]
    #print(content)

    #두 번째 방법 : map 함수를 사용해서 숫자 데이터를 문자열로 변환하기
    content = list(map(str, datas))
    print(content)

    #세 번째 방법 : 직접 for 문
    #content = []
    #for n in datas:
    #    content.append(str(n))
    #print(content)

    #리스트 --> '12,34,56,78,90'
    content = ','.join(content)
    print(content)
    
    try:
        with open("data.txt", 'wt', encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print(e)
        
main()

#텍스트로 되어있는 data.txt 파일을 읽어서 리스트로 복원 -> csvfile.py