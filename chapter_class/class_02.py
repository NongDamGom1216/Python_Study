class Human:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

    def __str__(self):
        return f'<Human name = {self.name}, age = {self.age}>'
        

def main():
    kim = Human("김상형", 29) #__init__() 호출
    kim.intro()
    lee = Human("이승우", 45)
    lee.intro()

    print(kim.name)
    print(kim.name, kim.age) # kim['name'], kim['age']

    print(kim) # kim.__str__() 호출, kim을 문자열로 호출
    print(lee)

main()

