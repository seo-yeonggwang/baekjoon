def cel(money):
    Quarter = money // 25
    Dime = (money - (Quarter * 25)) // 10
    Nickel = (money - (Quarter * 25) - (Dime * 10)) // 5
    Penny = (money - (Quarter * 25) - (Dime * 10) - (Nickel * 5))

    print(Quarter, Dime, Nickel, Penny)
    return 0

t = int(input())

for i in range(t):
    money = int(input())
    cel(money)