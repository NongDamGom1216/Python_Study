class Date:
    def __init__(self, month):
        self.inner_month = month

    @property #데코레이터
    def month(self): #읽기용(1번) getter 함수
        return self.inner_month 

    @month.setter #month property에 대한 setter를  표현하는 것
    def month(self, month): #쓰기용(2번) setter 함수
        if 1 <= month <= 12:
            self.inner_month = month

def main():
    today = Date(8)
    today.month = 15 # 멤버변수 month에 15를 대입해라(2번이 호출됨)
    print(today.month) # 멤버변수 month를 읽어라(1번이 호출됨)
    # 멤버 변수 month는 없다 --> property를 사용하여 month라는 함수를 변수처럼 사용

    today.month = 10
    print(today.month)

main()
