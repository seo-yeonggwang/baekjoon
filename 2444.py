N = int(input())  # N 입력받기

# 위쪽 삼각형 출력
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))

# 아래쪽 삼각형 출력
for i in range(N - 1, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))