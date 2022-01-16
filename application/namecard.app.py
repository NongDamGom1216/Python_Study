# 사전을 사용한 명함 관리 프로그램
# 관리할 명함 정보: 이름, 전화번호, email, 주소록

# 시작할 때 고려사항
# 1. 데이터를 어떻게 표현하고 관리할 것인가?
# 한 사람의 정보 :  사전
# 여러 명의 정보 :  리스트

# 2. 어떤 기능을 제공할 것인가?
# 목록(검색), 추가, 수정, 삭제 -> CRUD 연산(Create, Read, Update, Delete)

#command 키 누르면서 함수로 이동할수있음
#command + k + f 누르면 json 파일 내에서 정렬할 수 있음

import sys
import random
from file_util import load, save, load_json, save_json


books = []
FILE_NAME = "book.json"

def create_card(name, phone, email, address):
    return {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address" : address
    }

def init(): #초기화 함수
    """ for i in range(1, 11):
        card = create_card(f'가은{i:03}',f'010-1111-{i:04}', f'gaeun{i:03}@google.com', '카운터사이드')
        books.append(card)
    for i in range(11, 21):
        card = create_card(f'히나나{i:03}',f'010-1111-{i:04}', f'hinana{i:03}@google.com', '샤이니컬러즈')
        books.append(card)
    random.shuffle(books)
    """
    # 이름으로 정렬하세요.
    
    global books
    books = load_json(FILE_NAME) #global을 선언하지 않고 대입연산자로 변수를 사용하면 지역변수
    books.sort(key=lambda card : card["name"])

def print_menu():
    print()
    print('='*50)
    print('    목록    검색    추가    수정    삭제    종료')
    print('='*50)

def print_card_list(card_list):
    for ix, card in enumerate(card_list): # 인덱스 정보를 보여주기 위해 enumerate 사용한다.
        print(f'{ix:3}    {card["name"]}    {card["address"]}')
    print()
    print(f'총: {len(card_list)}명')

# 목록 메뉴 실행 함수
def print_list():
    print("목록보기")

    print_card_list(books)

# 검색 메뉴 실행 함수
def search():
    keyword = input("검색 이름: ")

    # 검색하고, 출력
    result = []
    """for card in books:
        if keyword in card["name"]:
            result.append(card)"""

    # 람다 함수를 이용한 filter
    result = list(filter(lambda card: keyword in card["name"], books))

    print_card_list(result)

# 추가 메뉴 실행 함수
def add_card():
    name = input("이름: ")
    phone = input("전화번호: ")
    email = input("email: ")
    address = input("주소 ")

    card = create_card(name, phone, email, address)
    books.append(card)
    books.sort(key=lambda card : card["name"]) #추가한 다음 이름으로 정렬


def find_by_name(name):
    # 찾았으면 인덱스 리턴, 못 찾았으면 -1 라턴
    for ix, card in enumerate(books):
        if card['name'] == name:
            return ix
    
    return -1 #for 문을 다 돌았는데도 못 찾았을 경우

def update_card():
    name = input("변경할 카드의 이름: ")
    ix = find_by_name(name)

    if ix != -1 :
        card = books[ix] #실제 데이터에 대한 참조
        print(card)

        name = input("변경할 이름: ")
        phone = input("변경할 전화번호: ")
        email = input("변경할 email: ")
        address = input("변경할 주소: ")

        if name != '':
            card['name'] = name
        if phone != '':
            card['phone'] = phone
        if email != '':
            card['email'] = email
        if address != '':
            card['address'] = address

        print(f'{name} 항목을 변경했습니다.')
        books.sort(key=lambda card : card["name"]) #추가한 다음 이름으로 정렬
        print(card)
    else:
        print("목록에 없는 이름입니다.")


def delete_card():
    name = input("삭제할 이름: ")
    ix = find_by_name(name)
    
    if ix != -1 :
        books.pop(ix) #del books[ix]
        print(f'{name} 항목을 삭제했습니다.')
    else:
        print("목록에 없는 이름입니다.")



# 종료 메뉴 실행 함수
def exit():
    print("정말 종료하시겠습니까")
    command = input("Y or N \n")
    if command == 'Y' or command == 'y': # answer.lower() == 'y' # answer in ['Y', 'y']
        
        #book.json 파일로 저장
        save_json('book.json', books)

        sys.exit(0)
    else:
        print("메인으로 이동합니다.")
        pass

        
def main():
    init()
    print()
    print("나의 여자친구 리스트")
    while True:
        # 메뉴 출력
        print_menu()
        # 사용자가 메뉴를 입력
        menu_item = input('선택: ')
        if menu_item == "목록":
            print_list()
        elif menu_item == "검색":
            search()
        elif menu_item == "추가":
            add_card()
        elif menu_item == "수정":
            update_card()
        elif menu_item == "삭제":
            delete_card()    
        elif menu_item == "종료":
            exit()
        else:
            print("메뉴를 다시 입력하십시오.")
        # 입력한 메뉴를 실행/결과 출력
        

main()
