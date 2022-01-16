# 애플리케이션 : Application
# 데이터 : 앱 이름, 메뉴
# 기능 : 메뉴 구성, 초기화, 종료, 운영

from menu import Menu
import sys

class Application:
    def __init__(self, title) -> None:
        self.title = title
        self.menu = Menu()

    # 메뉴 구성
    def create_menu(self):
        pass

    # 앱 초기화
    def init(self):
        self.create_menu()

    # 앱 종료
    def exit(self):
        answer = input('종료할까요? (y/n)').lower()
        if answer == 'y':
            sys.exit(0)
        else:
            pass
    
    # 앱 운영
    def run(self):
        self.init()
        while True:
            print(f'[{self.title}]')
            self.menu.print()
            item = self.menu.select()

            if item : #None이 아닐 경우 실행한다.
                item.run()
            else:
                print("잘못된 메뉴입니다.")
            
            print()