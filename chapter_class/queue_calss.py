# Queue : First In First Out
# 클래스 설계
#   클래스명 : Queue
#       데이터 : 리스트
#       기능 : 추가, 꺼내기, 비었는지 검사
# 클래스 설계 원칙 : SRP, 단일 책임의 원칙

class Queue:
    def __init__(self) -> None:
        self.data = []

    def put(self, value):
        self.data.append(value)
    
    def get(self): #메소드 내에서 다른 메소드를 호출할 때는 self.isEmpty
        assert not self.is_empty(), '큐가 비었습니다.'
        return self.data.pop(0)
    
    def read_bottom(self):
        assert not self.is_empty(), '큐가 비었습니다.'
        bottom = self.data[0]
        return bottom
    
    def is_empty(self): # is로 시작하는 함수의 return type은 bool이다.
        return len(self.data) == 0

def main():
    q = Queue()
    q.put(1)
    q.put(10)
    q.put("린제")

    print(q.get())
    print(q.get())
    print(q.get())

    if (not q.is_empty()):
        print(q.get())

main()