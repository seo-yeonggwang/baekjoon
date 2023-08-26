def palendrom():
    l = str(input())
    cheak(l)
    
    return 0

def cheak(arr):
    start = 0
    final = -1
    
    for i in range(len(arr)):
        if arr[start] == arr[final]:
            start +=1
            final -=1
        else:
            print("0")
            return 0
    print("1")
    
    return 0

palendrom()