# NameCard 데이터 클래스

# class NameCard:
#     def __init__(self, name, phone, email, address) -> None:
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address
    
#     def __repr__(self) -> str:
#         return f'NameCard(name = {self.name})'
    
#     def __str__(self) -> str:
#         return f'NameCard(name = {self.name}, phone = {self.phone}, email = {self.email}, address = {self.address})'


# 위 코드를 간편하게 할 수 있는 방법(생성자를 만들 필요가 없다)
from dataclasses import dataclass
import file_util
import os
from paging import Paginator

@dataclass # 데코레이터
class NameCard:
    name: str # 이 레벨에 있으면 클래스 변수
    phone: str = '' # default 값 지정 가능
    email: str = ''
    address: str = ''

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)

# json 모듈: 파이썬 표준 모듈만 처리 가능하다.

# NameCardBook 클래스: SRP 단일책임원칙
# NameCard 모델 클래스의 콜렉션 역할
# 데이터 : NameCard 목록
# 기능 : CRUD, 저장, 불러오기

class NameCardBook:
    def __init__(self) -> None:
        self.book = []

    def add(self, name, phone, email, address):
        card = NameCard(name, phone, email, address)
        self.book.append(card)
        self.book.sort(key=lambda card : card.name) #추가한 다음 이름으로 정렬

    def update(self, ix, name, phone, email, address):
        card = self.book[ix]
        card.name = name
        card.phone = phone
        card.email = email
        card.address = address

    def get(self, ix): #인덱스를 통하여 참조를 얻어내는 것
        return self.book[ix]

    def remove(self, ix):
        #ix = self.find(name) 매개변수가 name일 경우
        if ix != -1:
            self.book.pop(ix)
    
    def search(self, name):
        result = list(filter(lambda card: name in card.name, self.book))
        return result

    def find(self, name):
        # 찾았으면 인덱스 리턴, 못 찾았으면 -1 라턴
        for ix, card in enumerate(self.book):
            if card.name == name: #사전이랑 문법다른 거 확인하기
                return ix
    
        return -1 #for 문을 다 돌았는데도 못 찾았을 경우
    
    def load(self, file_path):
        # pickle로 한다.
        if os.path.exists(file_path):
            self.book = file_util.load(file_path)
        else:
            self.book = []

    def save(self, file_path):
        # pickle로 한다.
        file_util.save(file_path, self.book)
    
    # 페이지 목록 추출
    def get_page(self, page_num, count_per_page = 10): # 한 페이지당 몇 번
        page_obj = Paginator(self.book, page_num, count_per_page)
        return page_obj

    
if __name__ == '__main__': # 모듈 테스트
    import random # 테스트에서만 사용하기 때문에

    print('정렬 테스트')
    main_book = NameCardBook()
    main_book.add('신학', '010-1111-1111', 'shinhak@naver.com', '리월')
    main_book.add('루미네', '010-2222-2222', 'lumine@naver.com', '리월')
    main_book.add('히나나', '010-2222-2221', 'hinana@naver.com', '도쿄')
    print(main_book.book)

    print()
    print("-"*50)
    print()

    print('검색 테스트')
    result = main_book.search('학')
    print(result)
    result = main_book.search('루미')
    print(result)

    print()
    print("-"*50)
    print()

    print('find 테스트')
    ix = main_book.find('신학')
    print(ix)
    ix = main_book.find('히나나')
    print(ix)

    print()
    print("-"*50)
    print()

    print('삭제 테스트')
    main_book.remove(2)
    print(main_book.book)

    print()
    print("-"*50)
    print()

    # print('저장 테스트')
    # main_book.save('book.dat')

    # print()
    # print("-"*50)
    # print()

    # print('200개 데이터를 구성하여 book.dat로 저장')
    # main_book.book = []
    # addresses = ['도쿄', '오사카', '하라주쿠', '후쿠오카', '교토', '신주쿠']

    # for i in range(1, 101):
    #     main_book.add(f'히나나{i:03}', f'010-1111-{i:04}', f'hinana{i:03}@naver.com', random.choice(addresses))
    
    # main_book.save('book.dat')

