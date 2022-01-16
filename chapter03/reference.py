def modify(x):
    #x = [2, 3, 4 ,5] 이걸 추가하면 변경이 안되고 따로 출력된다.
    x[1] = 1000
    print(f'x: {x}')

def main():
    a = [10, 20, 30, 40] # x = a 가 실행된다.
    modify(a)

    print(f'a: {a}') #리스트이기 때문에 참조값이 넘어가서 변경되어 출력된다.

main()

print('-'*50)
#얕은 복사
list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy() # 얕은 복사(참조를 따라가지 않는다. swallow copy)

list2[0][1] = 'c' #list2[0]이 list0을 참조하고 있다.
list2[1]= 1000

print(list1)
print(list2)

print('-'*50)
#깊은 복사
import copy

list0 = ['a', 'b']
list1 = [list0, 1, 2]

list2 = copy.deepcopy(list1) # 깊은 복사
list2[0][1] = 'c'
list2[1]= 1000

print(list1)
print(list2)

#얕은 복사는 객체를 새로운 객체로 복사하지만 원본 객체의 주소값을 복사하는 것이고
#깊은 복사는 전체 복사로 참조값의 복사가 아닌 참조된 객체 자체를 복사하는 것을 말한다.