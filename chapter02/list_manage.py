#begin과 end를 같은 값을 주게 되면 기존 값이 대체되는 것이 아니라 삽입을 할 수 있다.
nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92] # 새로운 값들을 삽입
print(nums)

nums = [1, 2, 3, 4]
nums[1:3] = [90, 91, 92] #1,2를 교체
print(nums)

nums = [1, 2, 3, 4]
nums[1:3] = [] #1,2를 삭제
print(nums)

#이렇게 하면 이중 리스트가 됨, 리스트가 하나의 엘리먼트가 될 수 있다.
nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92] # 지정한 위치의 엘리먼트에 리스트 대체
print(nums)

#리스트 연결
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
list1.extend(list2)
print(list1)