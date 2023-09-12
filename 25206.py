sum = 0

for i in range(20):
    Subject,Score,StudyScore = map(str, input().split())

    if StudyScore == 'A+':
        StudyScore = float(4.5)
    elif StudyScore == 'A0':
        StudyScore == float(4.0)
    elif StudyScore == 'B+':
        StudyScore == float(3.5)
    elif StudyScore == 'B0':
        StudyScore == float(3.0)
    elif StudyScore == 'C+':
        StudyScore == float(2.5)
    elif StudyScore == 'C0':
        StudyScore == float(2.0)
    elif StudyScore == 'D+':
        StudyScore == float(1.5)
    elif StudyScore == 'D0':
        StudyScore == float(1.0)
    elif StudyScore == 'A0':
        StudyScore == float(0.0)
    else:
        break
    
    sum += float(Score) * StudyScore
    print(sum)