# 이 모듈에서 만들어준 book.dat로 해야 정상적으로 열린다.

from namecard import NameCardBook
import random

def main():
    book = NameCardBook()

    print('200개 데이터를 구성하여 book.dat로 저장')
    book.book = []
    addresses = ['도쿄', '오사카', '하라주쿠', '후쿠오카', '교토', '신주쿠']

    for i in range(1, 101):
        book.add(f'히나나{i:03}', f'010-1111-{i:04}', f'hinana{i:03}@naver.com', random.choice(addresses))
    
    # book.book을 orderby 변수의 값을 기준을 정렬
    
    # 이름으로 정렬
    orderby='name'
    book.book.sort(key = lambda card : card[orderby])
    print(book.book)
    book.save('book.dat')

main()