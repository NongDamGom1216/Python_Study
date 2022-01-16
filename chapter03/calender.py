import calendar as cal
dates = ["월", "화", "수", "목", "금", "토", "일"]
day = cal.weekday(2020, 8, 15)
print("광복절은 %s요일입니다."%dates[day])