while True:
    str = "89"
    try:
        score = int(str)
        print("입력한 점수 :", score)
        #a = str[1]
        #a = str[2] # 두 자릿 수를 입력할 경우 인덱스 에러
        break
    except ValueError:
        print("점수 형식이 잘못되었습니다.")
    except IndexError:
        print("첨자 범위를 벗어났습니다.")
        
print("작업완료")

print('-'*100)

#시스템의 에러 메시지 확인 방법

import traceback

mode = "DEV" #개발모드 설정
# DEV, PRODUCT

def convert(value):
    return int(value)

def work():
    str = "89점"
    score = convert(str)
    print(score)

def main():
    try:
        work()

    except Exception as e: #모든 예외에 대해서 처리할 때는 Exception
        print(e)
        if mode == "DEV":
            traceback.print_exc() #어떤 점에서 예외 처리를 하였는지 알 수 있다.

    print("작업완료")
main()

#try-except-finally 가능
#try-finally도 가능
#try만 단독으로는 쓸 수 없다