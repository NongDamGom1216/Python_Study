#여기서 len, max, min은 함수이고
#.index는 메소드이다.

def main():
    score = [88, 95, 70, 100, 99, 88, 78, 50]
    print(f"학생수는 {len(score)}명 입니다.")
    print(f"최고 점수는 {max(score)}점 입니다.")
    print(f"최고 점수는 {max(score)}점은 {score.index(max(score))}번째 데이터에 있습니다.")
    print(f"최소 점수는 {min(score)}점 입니다.")

main()

#입력받은 학생의 점수를 나타내는 방법, index 사용
def main2():
    names = ["히나나", "가은", "신학", "요이미야"]
    scores = [90, 80, 50, 30]
    
    name = input("검색이름: ")
    
    if name in names: #리스트에 없는 이름이면 에러가 나기 때문에 확인해줘야 함
        name_index = names.index(name)
        score = scores[name_index]
        print(f'입력받은 이름: {name}, 학생의 점수: {score}')
    else:
        print(f'{name}은 다른 학생입니다.')

main2()