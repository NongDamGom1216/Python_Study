#IoT에서 카메라를 설계할 때 사용

nums  = [11, 22, 33]
it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)

#이 구조는 다음과 같다.
#for num in nums:
#    print(num)

print()
print('-'*30)

# 예시
class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        self.index = -2 # 이걸 추가해주면 몇 번 루프를 돌아도 출력되게 한다.
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index:self.index+2]

solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ',')

print()
print('-'*30)

for k in solarterm:
    print(k, end = ',')

print()
print('-'*30)

#제너레이터
#yield를 사용하면 데이터를 연속해서 return
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
# 함수 내에서 yield 예약어가 사용된 경우
# 함수가 실행되는게 아님
# generator 객체가 만들어지게 됨

print(solarterm)

for k in solarterm:
    print(k, end = ',')