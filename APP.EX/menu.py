# 메뉴의 개념 --> 클래스로 표현
# 데이터 : 타이틀, 메뉴 함수에 대한 참조
# 기능 : 메뉴 함수 실행 

class MenuItem:
    def __init__(self, title, func) -> None:
        self.title = title
        self.func = func

    def run(self):
        self.func()

# 메뉴 Menu
# 데이터 : MenuItem의 collection --> 사전으로 관리
# 기능 : 선택, 메뉴 보여주기, 메뉴 추가하기

class Menu:
    def __init__(self) -> None:
        self.menus = {}
    
    def add_menu(self, title, func):
        item = MenuItem(title, func)
        self.menus[title] = item
    
    def print(self):
        titles = self.menus.keys() #사전에서 key 뽑기
        print('='*38)
        print('  '.join(titles))
        print('='*38)

    def select(self):
        choice = input('선택 : ') # 사전의 key를 입력
        item = self.menus.get(choice) #key를 잘못 입력하면 None
        return item

# 한 번에 주석 처리 command + /
# Menu


if __name__ == "__main__" :
    def print_list():
        print('print_list 실행')

    def play():
        print("실행")

    def exit():
        print("종료")

    menu = Menu()
    menu.add_menu('목록', print_list)
    menu.add_menu('재생', play)
    menu.add_menu('종료', exit)

    menu.print()
    item = menu.select() # item : Menuitem
    item.run()