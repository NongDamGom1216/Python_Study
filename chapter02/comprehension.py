#[수식 for 변수 in 리스트 if 조건]
nums = [ n*2 for n in range(1, 11)]
print(nums)
#for i in nums:
#    print(i, end = ', ')

#같은 결과
nums = []
for n in range(1, 11):
    nums.append(n*2)
print(nums)

print([n for n in range(1, 11) if n % 3 == 0]) #3의 배수만 리스트의 element로 추가


#음수 또는 100을 초과하는 데이터를 제외한 합계를 구하시오.
def main():
    scores = [70, 30, -10, 100, 160, 90]
    valid_score = [n for n in scores if n >= 0 and n <= 100]
    print(valid_score)
    print(sum(valid_score))

main()