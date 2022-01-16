# 클래스를 사용한 명함 관리

# 데이터(명함)를 표현하는 클래스 --> 데이터 클래스, 모델 클래스
class NameCard:
    def __init__(self, name, phone, email, address) -> None: #생략해도 상관없음, return 타입을 나타냄
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f'<NameCard name = {self.name} phone = {self.phone} email = {self.email} address = {self.address}>'

    def __repr__(self) -> str: # represent(대표 정보를 나타냄)
        return f'<NameCard name = {self.name}>'
    

def main():
    """
    card1 = NameCard('히나나', '010-5100-3557', 'hyun5735@naver.com', 'Tokyo')
    card2 = NameCard('요이미야', '010-1234-3557', 'hyunj5735@daum.net', 'Inazuma')
    
    print(card1) # 클래스 안에서 __str__을 정의 안 해줄 경우 그냥 주소값(참조값)이 출력됨

    book = [card1, card2] # 클래스 안에서 __repr__을 정의 안 해줄 경우 주소값(참조값) 리스트가 출력됨
    print(book)
    """
    book = []
    for i in range(10):
        card = NameCard(f'히나나{i:03}', '010-5100-{i:04}', 'hyun{i:03}@naver.com', 'Tokyo')
        book.append(card)
    print(book)

main()

    

