#get을 쓰면 사전에 없는 단어여도 에러가 나지 않는다.
dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }

print(dic.get('boy'))
print(dic.get('girl'))
print(dic.get('girl', '사전에 없는 단어입니다.'))

print('-'*20)

dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }
dic['boy'] = '남자아이'
dic['girl'] = '소녀'
del dic['book']
print(dic)

print('-'*20)

dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }
print(dic.keys())
print(dic.values())
print(dic.items())

print('-'*20)

dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }
keylist = dic.keys()

for key in keylist:
    print(key, dic[key])

print()

dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }

for key, value in dic.items():
    print(f'{key}: {value}')

print('-'*20)

dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
    }

#dic.keys는 리스트가 아니기 때문에 리스트로 만들어줬다.
li = list(dic.keys()) #dic.keys는 리스트가 아니기 때문에 리스트로 만들어줬다.
print(li)

li = list(dic)
print(li)

print('-'*20)

#2개의 사전을 합친다. book이라는 key가 겹친다.
dic = { 'boy': '소년', 'school': '학교', 'book':'책'}
dic2 = { 'student': '학생', 'teacher': '선생님', 'book':'서적'}
dic.update(dic2) #뒤에 있는거로 업데이트
print(dic)

print('-'*20)

#이런 구조일 경우에만 리스트에서 사전으로 변환이 가능하다.
li = [
['boy', '소년'],
['school', '학교'],
['teacher', '선생님']
]
dic = dict(li)
print(dic)