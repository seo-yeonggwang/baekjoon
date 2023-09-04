def factorial(N):
    sum = 1
    for i in range(1,N+1):
        sum *= i

    print(sum)

N = int(input())
factorial(N)