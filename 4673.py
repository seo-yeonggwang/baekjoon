def SelfNumber():
    number = set(range(1, 10001))
    SelfNumber = set()

    for i in range(10001):
        SelfNumber.add(d(i))

    SelfNumber = number - SelfNumber

    for num in sorted(SelfNumber):
        print(num)

def d(n):
    sum = n
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

SelfNumber()