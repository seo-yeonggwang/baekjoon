def hop(N):
    arr = str(input())
    sum = 0
    
    for i in range(N):
        sum += int(arr[i])
        
    print(sum)    
    
    return 0

N = int(input())
hop(N)