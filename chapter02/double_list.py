score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]

total = 0
totalsub =0

for student in score:
    subject_total = 0
    for subject in student:
        subject_total += subject

    subjects = len(student)
    print(f"총점 {subject_total}, 평균 {subject_total/subjects:.2f}" )

    total += subject_total
    totalsub += subjects

print(f"전체평균 {total/totalsub:.2f}")