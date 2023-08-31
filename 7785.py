def work(InOut):
    arr = [0] * InOut
    arr2 = [0] * InOut
    working = set()

    for i in range(InOut):
        arr[i], arr2[i] = map(str,input().split())

    for name in range(InOut):
        if arr2[name] == "enter":
            working.add(arr[name])
        elif arr2[name] == "leave" and name in working:
            working.remove(arr[name])

    WorkingList = sorted(working, reverse = True)

    for name in WorkingList:
        print(name)

InOut = int(input())
work(InOut)