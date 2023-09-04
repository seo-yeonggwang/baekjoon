def apt(test):
    house = [[0] * 14 for i in range(15)] # y축 15, x축 14

    for i in range(1,15): # 0층 인원 초기화
        house[0][i-1] = i

    for i in range(1, 15):
        for j in range(14):
            house[i][j] = house[i][j-1] + house[i-1][j]

    for j in range(test):
        k = int(input())
        n = int(input())
        check(k,n, house)
    
def check(k,n, house):
    print(house[k][n-1])

test = int(input())
apt(test)