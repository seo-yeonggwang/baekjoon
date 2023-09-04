from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N+1))
result = []

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")