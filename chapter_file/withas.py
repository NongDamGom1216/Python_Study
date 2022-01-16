#with~as를 사용하면 명시적으로 close() 함수를 호출하지 않아도 파일이 항상 닫힌다.
# 'r' -> 디폴트가 텍스트 모듈이라는 뜻

#텍스트 파일을 읽어서 내용을 리턴하는 함수를 작성하시오.

def load(filename):
    try: 
        with open(filename, 'r', encoding="utf-8") as file:
            str = file.read()
            return str
    except:
        return '' # 열고자 하는 파일이 폴더에 없을 때 빈 문자열을 리턴한다.(메인 함수가 멈추지 않게)

"""
try:
    content = load("live.txt")
    print(content)
except Exception as e:
    print(e)
#file.close()
"""

print("-"*100)

#파일명과 내용을 전달받아 내용을 추가하여 지정한 파일로 저장하는 함수

def save(filename, content):
    with open(filename, 'wt', encoding="utf-8") as file:
        file.write(content)

def main():
    try:
        file_name = 'live.txt'
        content = load(file_name) #여기서 아무것도 추가안하고 저장하면 그냥 파일 복사
        
        #내용 수정
        str = input("추가할 내용 입력: ")
        content += str + '\n'

        save("withas.txt", content)
        print(content)

    except Exception as e:
        print(e)

main()