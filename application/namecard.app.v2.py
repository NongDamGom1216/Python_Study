# 클래스를 이용하여 다시 만들기
# NameCard : 데이터 클래스(모델 클래스)
# NameCardBook : NameCard 모델의 컬렉션 클래스

# Application : 운영 클래스
# 데이터 : 앱 타이틀, NameCardBook, 파일명

from namecard import NameCardBook
from baseapp import Application #mylib

class NameCardBookApp(Application):
    def __init__(self) -> None:
        super().__init__("명함 관리 앱")
        self.book = NameCardBook()
        self.FILE_PATH = 'book.dat'

    def init(self):
        super().init() # 메뉴 구성
        # book.dat를 불러온다.
        self.book.load(self.FILE_PATH)
        print(self.book.book)
    
    def print_card_list(self, card_list, start = 0):
        print('-'*40)
        for ix, card in enumerate(card_list, start):
            print(f'{ix+1:3} {card["name"]} {card["address"]}')
        print('-'*40)


    def print(self):
        while True:
            # 페이지 단위로 출력
            page_num = int(input('페이지 번호: '))
            
            if page_num == 0:
                break

            # 해당 페이지를 출력
            page_obj = self.book.get_page(page_num)

            self.print_card_list(page_obj.page, page_obj.start)
            print(f'[{page_num}/{page_obj.total_page}]')
            print(f'페이지 내의 명함 갯수 : {page_obj.total_page}')
            print(f'총 명함 갯수 : {page_obj.total_count}')

            print('0을 누르면 종료합니다.')

        print()

    def add(self):
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("email: ")
        address = input("주소 ")

        self.book.add(name, phone, email, address)

    def get_field(self, card, key, title):
        value = input(f'{title} {card[key]} : ')
        if value == '': # 수정할 이름을 적지 않으면 그대로
            value = card[key]
        return value

    def update(self):
        name = input('수정할 이름: ')
        ix = self.book.find(name)

        if ix != -1:
            card = self.book.get(ix)
            name = self.get_field(card, 'name', '이름')
            phone = self.get_field(card, 'phone', '번호')
            email = self.get_field(card, 'email', '이메일')
            address = self.get_field(card, 'address', '주소')
            self.book.update(ix, name, phone, email, address)
        else:
            print(f'{name}에 대하여 다시 입력하십시오.')


    def search(self):
        keyword = input("검색 이름: ")
        result = self.book.search(keyword)
        self.print_card_list(result)
        print(f'총 {len(result)} 명')

    def remove(self):
        name = input("삭제할 이름: ")
        ix = self.book.find(name)
        
        if ix != -1 :
            self.book.remove(ix) #del books[ix]
            print(f'{name} 항목을 삭제했습니다.')
        else:
            print("목록에 없는 이름입니다.")

    def exit(self):
        super().exit(lambda : self.book.save(self.FILE_PATH))

    def create_menu(self):
        self.menu.add_menu('목록', self.print)
        self.menu.add_menu('추가', self.add)
        self.menu.add_menu('수정', self.update)
        self.menu.add_menu('검색', self.search)
        self.menu.add_menu('삭제', self.remove)
        self.menu.add_menu('종료', self.exit)

def main():
    app = NameCardBookApp()
    app.run()

main()