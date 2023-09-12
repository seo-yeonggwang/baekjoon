information, math, science, english = map(int, input().split())
information2, math2, science2, english2 = map(int, input().split())

sum1 = information + math + science + english
sum2 = information2 + math2 + science2 + english2

if sum1 != sum2:
    print(max(sum1,sum2))
else:
    print(sum1)