# 스택
# 클래스 설계할 때 : 다루는 데이터가 무엇인가?, 그 데이터를 어떻게 운영하는가?
# list로 관리, 저장, 꺼내기, 꺼내지 않고 top만 읽기

class Stack:
    def __init__(self) -> None:
        self.data = []
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        assert len(self.data) > 0, '스택이 비었습니다.' #assert는 예외를 발생시킨다, 참이면 통과한다.
        return self.data.pop()
    
    def read_top(self):
        assert len(self.data) > 0, '스택이 비었습니다.'
        top = self.data[-1] #top = len(self.data) - 1
        return top
    
    def is_empty(self): # is로 시작하는 함수의 return type은 bool이다.
        return len(self.data) == 0

def main():
    stack = Stack()

    stack.push(10)
    stack.push("히나나")
    stack.push(100)

    print(stack.read_top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

main()