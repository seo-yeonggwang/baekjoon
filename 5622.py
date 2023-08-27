def time(arr):
    sum = 0
    
    for i in range(len(arr)):
        if arr[i] in ("A", "B", "C"):
            sum += 3
        elif arr[i] in ("D", "E", "F"):
            sum += 4
        elif arr[i] in ("G", "H", "I"):
            sum += 5
        elif arr[i] in ("J", "K", "L"):
            sum += 6
        elif arr[i] in ("M", "N", "O"):
            sum += 7
        elif arr[i] in ("P", "Q", "R", "S"):
            sum += 8
        elif arr[i] in ("T", "U", "V"):
            sum += 9
        elif arr[i] in ("W", "X", "Y", "Z"):
            sum += 10
    print(sum)

arr = []
arr = str(input())

time(arr)