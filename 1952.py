def add(p1, p2):
    return [p1[0] + p2[0], p1[1] + p2[1]]

turn = 0
count = 0
m, n = input().split()
m = int(m)
n = int(n)
data = [[0] * n for _ in range(m)]
direction = [[0,1],[1,0],[0,-1],[-1,0]] # 방향
dir = 0 # 방향 변환을 위한 변수(나머지 % 활용)
curr = [0,0] # 현재 위치

while True:
    data[curr[0]][curr[1]] = 1
    next = add(curr, direction[dir])
    if next[0]==-1 or next[0]==m or next[1]==-1 or next[1] == n or data[next[0]][next[1]]==1:
        dir = (dir+1)%4
        count = count+1
        turn = turn + 1
    else:
        curr = next
        turn = 0
    if turn==2:
        count = count - 2
        break
print(count)

