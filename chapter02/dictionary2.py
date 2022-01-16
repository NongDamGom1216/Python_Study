users = [
    #회원정보 표현하는 예시
    {
        'name': '히나나',
        'age' : 16,
        '주소' : '도쿄'
    },
    {
        'name': '신학',
        'age' : 26,
        '주소' : '노엘'
    },
    {
        'name': '노엘',
        'age' : 22,
        '주소' : '몬드'
    },
]

for user in users:
    print(f"{user['name']}\t{user['age']}\t{user['주소']}")


print('-'*20)
print()

#알파벳 빈도수 사전 활용해서 찾기
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
print(alphabet)

key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=>', num)

for code in range(ord('a'), ord('z')+1):
    c = chr(code)
    num = alphabet.get(c, 0)
    print(c, '=>', num)