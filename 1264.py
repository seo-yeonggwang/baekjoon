arr = []

while(True):
    arr = str(input())
    arr = arr.lower()
    if arr[0] == '#':
        break
    print(arr.count('a') + arr.count('e') + arr.count('i') + arr.count('o') + arr.count('u'))