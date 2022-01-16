names = ['가은이', '서윤이', '히나나', '하지메']

#이름을 입력받아서 리스트에 이름이 있는지 판단
#exit 단어 입력되면 종료
while True:
    search_name = input("이름 입력: ")
    search_result = 0
    count = 0

    if search_name == 'exit' :
        break

    for x in names:
        if x == search_name:
            print("찾았습니다.")
            search_result = 1
            break
        count += 1 # 몇 번째에 있는지 구하기 위해서    
    
    if search_result == 1:
        print('찾은 이름: ', search_name, (count+1), '번째에 있습니다.')
    else:
        print('리스트에 없습니다.')
