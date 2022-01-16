#앞에서부터 012~
#만약 음수부터면 뒤에서부터 -1 -2 ~ (음수는 0부터 시작안함!)
#step의 기본값 1, begin의 기본값 0, end의 기본값 -1(맨끝)
#맨 뒤는 포함안됨!!!

s = "0123456789.jpg"
print(s[2:5]) #234
print(s[3:]) #3456789.jpg
print(s[:3]) #012
print(s[-3:]) #jpg

#헷갈리지 않기 위한 tip -> end = begin + 데이터갯수
# 5 = 2 + 3(데이터갯수)

#함수명은 보통 동사형으로 한다.
def get_year_str(file_name):
    print("촬영 년도 : " + file_name[0:4] + "년")

def get_date_str(file_name):
    print("촬영 날짜 : " + file_name[4:6] + "월" + file_name[6:8] + "일")

def get_time_str(file_name):
    print("촬영 시간 : " + file_name[9:11] + "시간" + file_name[11:13] + "분" + file_name[13:15] + "초")

def main():
    #날짜파트-시간파트
    file = "20220101-105030.jpg"
    year_str = get_year_str(file)
    date_str = get_date_str(file)
    time_str = get_time_str(file)

main()

#유용한 기능
dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])