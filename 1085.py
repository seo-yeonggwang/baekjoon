x, y, w, h = map(int,input().split())
start = [x,y]
line = [w,h]

answer = min(abs(x-w),abs(y-h), x, y)
print(answer)