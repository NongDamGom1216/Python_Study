#데이터클래스 사용해서 응용하는 법

from dataclasses import dataclass

@dataclass
class NameCard:
    name: str
    phone: str = ''
    email: str = ''
    address: str = ''

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)

def main():
    card = NameCard('히나나', '010-5100-3557')
    print(card)

    name = getattr(card, 'name') #조사하고 싶은 객체의 인스턴스, name = card.name과 같다.
    print(name)

    setattr(card, 'email', 'hinana@naver.com') # card.email = 'hinana@naver.com'
    print(card)

    key = 'name'
    value = getattr(card, key) #값을 얻을 때
    print(value)
    print(card[key]) #__getitem__(self, key)

    key = 'address'
    value = '서울시'
    setattr(card, key, value) #값을 설정할 때
    print(card)
    card[key] = '제주도' #__getitem__(self, key, value)
    print(card)

main()