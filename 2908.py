def sang(N,M):
    N = change(N)
    M = change(M)
    
    print(max(N,M))
    
    return 0

def change(Num):
    hun = Num // 100
    Num -= (hun * 100)
    ten = Num // 10
    Num -= (ten * 10)
    one = Num
    
    sum = one * 100 + ten * 10 + hun
    
    return sum
    

N,M = map(int, input().split())
sang(N,M)