def dice(Num1, Num2, Num3):
    if Num1==Num2==Num3:
        price = 10000 + Num1*1000
    elif Num1 == Num2 or Num1 == Num3:
        price = 1000 + Num1*100
    elif Num2 == Num3:
        price = 1000 + Num2*100
    else:
        price = max(Num1, Num2, Num3) * 100

    print(price)
    
    return 0

Num1, Num2, Num3 = map(int, input().split())
dice(Num1,Num2,Num3)