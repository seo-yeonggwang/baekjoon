def emotion(l):
    sad = 0
    happy = 0
    count = 0

    for i in l:
        if i == ':':
            count = 1
        elif count == 1 and i == '-':
            count = 2
        elif count == 2 and i == '(':
            sad += 1
        elif count == 2 and i == ')':
            happy += 1
        else:
            count = 0
    if sad > happy:
        print("sad")
    elif happy > sad:
        print("happy")
    elif sad == 0 and happy == 0:
        print("none")
    elif sad == happy:
        print("unsure")

    return 0

l = str(input())
emotion(l)