import random
food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

print(random.sample(food, 2))


nums = random.sample(range(1, 46), 6) #1 ~ 45개의 숫자 중 6개 리턴
nums.sort()
print(nums)