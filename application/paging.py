# 페이지 정보를 가지는 클래스
# 데이터 : 페이지에 담길 데이터, 페이지 번호, 전체 데이터 건수, ......

import math

class Paginator:
    def __init__(self, data, page_num, count_per_page) -> None:
        self.total_count = len(data)
        self.page_num = page_num
        self.total_page = math.ceil(self.total_count / count_per_page)
        
        #math 함수를 써서 반올림을 해줘야 한다.
        #page_num은 내가 보고싶어하는 페이지 넘버
        self.start = (self.page_num-1)*count_per_page
        self.end = self.start + count_per_page
        self.page = data[self.start:self.end] #슬라이싱