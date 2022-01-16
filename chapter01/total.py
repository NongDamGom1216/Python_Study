#1부터 100까지의 합
num = 1
total = 0
while num <= 100:
    total += num
    num += 1

print("total =", total)

#홀수의 합
num = 1
odd_total = 0
while num <= 100:
    odd_total += num
    num += 2

print("total =", odd_total)

#짝수의 합
num = 2
even_total = 0
while num <= 100:
    even_total += num
    num += 2

print("total =", even_total)

#같이 나타내기
number = 1
oddtotal = 0
eventotal = 0

while number <= 100:
    if number % 2 ==0:
        eventotal += number
    else:
        oddtotal += number
    
    number += 1

print("짝수의 합: ", eventotal)
print("홀수의 합: ", oddtotal)