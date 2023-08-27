def roof(num):

    for i in range(num):
        n, arr = input().split()

        for j in range(len(arr)):
            for z in range(int(n)):
                print(arr[j], end = "")
        print()

    return 0

num = int(input())
roof(num)