def calc_sum(list):
    total = 0
    for s in list:
        total += s
    return total

def get_score(subject, scores):
    total = calc_sum(scores)
    print(f"{subject} 총점: {total}")
    print(f"{subject} 평균: {total/len(scores):.2f}")

def main():
    english_score = [88, 95, 70, 100, 99]
    korean_score = [98, 56, 30, 63, 77]

    get_score("영어", english_score)
    get_score("국어", korean_score)
    
main()