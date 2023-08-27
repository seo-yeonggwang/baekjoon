def back(n):
    for i in range(n):
        arr = str(input()).split()

        for j in range(len(arr)):
            read(arr[j])
            print(" ",end = "")
        print()
    return 0

def read(arr):
    count = -1
    for i in range(len(arr)):
        print(arr[count], end = "")
        count -= 1

n = int(input())
back(n)