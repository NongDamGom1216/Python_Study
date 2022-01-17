# with open() as f
 
# Context Manager 객체
# __enter__ (self) 메소드 : with로 객체를 만들어서 as에 배정할 때 호출. 리턴값이 as 변수에 대입
# __exit__(self, type, value, tb): with 코드 블록을 벗어날 때 호출

class Myobject:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print('with 코드 블록에 진입합니다.')
        return self
    
    def __exit__(self, type, value, tb):
        print('with 코드 블록을 벗어납니다.')
        print('클린업 정리 작업 수행')

def main():
    with Myobject() as obj:
        input('마치려면 enter')
    
    print('작업 완료')

main()
