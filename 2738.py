def hop(N,M):
    arr1 = []
    arr2 = []
    result = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        arr1.append(row)
    for j in range(N):
        row = list(map(int, input().split()))
        arr2.append(row)
        
    for i in range(N):
        result_box = []
        for j in range(M):
            result_box.append(arr1[i][j] + arr2[i][j])
        result.append(result_box)
                     
    for row in result:
        print(*row)
        
    return 0

N, M = map(int, input().split())
hop(N,M)