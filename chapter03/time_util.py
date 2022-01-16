#시간 출력할 때 많이 쓰인다.
import time
t = time.time()
print(time.ctime(t))

print('-'*50)

import time
now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

print('-'*50)

from datetime import datetime
now = datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))

print('-'*50)

# 다음 함수를 정의하세요.
# 리턴값 : 20220110-130103.jpg(현재날짜-시간.jpg)

def get_measure_time(func): #함수를 매개변수로 전달 받음
    start = time.time()
    func() # 매개변수로 전달받은 함수를 실행
    end = time.time()
    return end - start

def get_time_filename(ext, seq=1):
    now = datetime.now()
    file_name = (f'{now.year}{now.month:02}{now.day:02}-{now.hour:02}{now.minute:02}{now.second:02}-{seq:03}.{ext}')
    #02 03 등으로 자릿수 지정
    return file_name

def capture(seq=1): #파읾명을 위한 변수 seq
    file_name = get_time_filename('jpg', seq)
#카메라 촬영하고 이미지를 지정한 파일명으로 저장
    return file_name

def main():
    for ix in range(5):
        file_name = capture(ix+1)
        print(file_name)
        time.sleep(0.2)

main()