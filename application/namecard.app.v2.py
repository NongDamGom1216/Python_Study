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
    
    def print(self):
        # 페이지 단위로 출력
        page_num = int(input('페이지 번호: '))
        # 해당 페이지를 출력
        page, total_page = self.book.get_page(page_num)
        print(page)
        print(total_page)

    def add(self):
        pass

    def update(self):
        pass

    def search(self):
        pass

    def remove(self):
        pass

    def create_menu(self):
        self.menu.add_menu('목록', self.print)
        self.menu.add_menu('추가', self.add)
        self.menu.add_menu('수정', self.update)
        self.menu.add_menu('검색', self.search)
        self.menu.add_menu('삭제', self.remove)
        self.menu.add_menu('종료', super().exit)

def main():
    app = NameCardBookApp()
    app.run()

main()