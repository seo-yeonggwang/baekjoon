def inputing(N,M):
    arr1 = [list(map(int,input())) for i in range(N)]
    arr2 = [list(map(int,input())) for i in range(N)]

    change(arr1,arr2)

    return 0

def change(arr1, arr2):
    count = 0
    for i in range(N-2):
        for j in range(M-2):
            if arr1[i][j] != arr2[i][j]:
                for x in range(i,i+3):
                    for y in range(j, j+3):
                        if arr1[x][y] == 1:
                            arr1[x][y] = 0
                        elif arr1[x][y] == 0:
                            arr1[x][y] = 1
                count +=1
    if arr1 == arr2:
        print(count)
    return 0

N, M = map(int, input().split())
inputing(N,M)