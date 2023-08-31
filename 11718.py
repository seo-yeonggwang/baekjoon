def copy():
    while(True):
        try:
            print(input())
        except EOFError:
            break
    return 0

copy()