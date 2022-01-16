#모든 클래스는 object 클래스의 자식이다.

class Human:
    def __init__(self, name, age):
            self.name = name
            self.age = age
    
    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

    def eat(self):
        print("케이크를 먹습니다.")
    
    def __str__(self): #오버라이딩
        return f'Human(name = {self.name}, age = {self.age})'

class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age) #super()는 상위 인스턴스를 참조, 상속을 할 때는 항상 상위 클래스 초기화 함수를 사용해야함
        self.stunum = stunum
    
    def intro(self):
        super().intro() #상위 클래스에서 정의한 intro()를 재정의 -> 오버라이딩(중요), 함수이름과 매개변수가 똑같아야 한다!!!
        print("학번: " + str(self.stunum))
    
    def study(self):
        print("Hello world를 SNS에 쓰는 사람들은 문과다.")

class Producer(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def produce(self):
        print("프로듀싱을 합니다.")
    
def main():
    hinana = Human("히나나", 21)
    hinana.intro()
    hinana.eat()

    print("-"*50)

    koito = Student("코이토", 17, 230101)
    koito.intro()
    koito.study()
    koito.eat()

    print("-"*50)

    jeong = Producer("제이", 25)
    jeong.intro()
    jeong.produce()
    jeong.eat()

    print(jeong) #__str__()가 호출됨
                 #제일 상위 클래스인 object 클래스에서 상속받은 것이다.

main()