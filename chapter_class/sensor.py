# 온도 센서(온도계)
# 클래스명 : Temperature
# 데이터 : 온도(value), 기록, 위치
# 기능 : 측정, 범위 초과시 예외

import random
from datetime import datetime
import time

class Temperature:
    def __init__(self, location, min_value, max_value) -> None:
        self.value = None
        self.records = []
        self.location = location
        self.min_value = min_value
        self.max_value = max_value
    
    def measure(self):
        # min_value, max_value 사이의 랜덤한 값으로 측정
        # 값은 소수점 둘째 자리 -> round
        self.value = round(random.uniform(self.min_value, self.max_value), 2)

        now = datetime.now()
        self.records.append((now, self.value))

        return now, self.value # 튜플로 리턴한다.
    
    # 히터
    # 클래스: Heater
    # 데이터 : 만든 온도계, 장소
    # 동작/기능 : 켜기, 끄기, 운영, 온도 설정

class Heater:
    def __init__(self, location) -> None:
        self.temp = Temperature(location, -5, 35) # 다른 클래스를 멤버 변수로 구성시켰다.
        self.location = location
        self.criteria = 19 #기준
        self.status = False # 디폴트가 꺼짐
    
    def turn_on(self):
        self.status = True
        print(f'보일러 켜짐 {self.temp.value}도')
    
    def turn_off(self):
        self.status = False
        print(f'보일러 꺼짐 {self.temp.value}도')
    
    def run(self):
        #온도를 측정해서, 기준 온도에 따라 보일러 켜기/끄기
        now, temp = self.temp.measure()
        if temp < self.criteria and self.status == False:
            self.turn_on()
        elif temp >= self.criteria and self.status == True:
            self.turn_off()
        else:
            pass
    
    def set_criteria(self, temp):
            set.criteria = temp


def main():
    # 1초 간격으로 온도를 측정해서 장소, 측정한 시간, 온도를 출력
    room_temp = Temperature('안방', -5, 35)
    room_Heater = Heater('안방')
    while True:
        time.sleep(1)
        now, value = room_temp.measure()
        room_Heater.run()
        print(f'{room_temp.location} {now} {value}')



main() 