import sys
input = sys.stdin.readline

n = int(input())
move = input().split()

x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
side = 0
for i in move :
    if i == 'L' :
        side = 0
    elif i == 'R' :
        side = 1
    elif i == 'U' :
        side = 2
    else :
        side = 3
    
    nx = x + dx[side]
    ny = y + dy[side]

    if nx < 0 or nx > (n-1) or ny < 0 or ny > (n-1) :
        continue

    x += dx[side]
    y += dy[side]

print(str(y+1) + ' ' + str(x+1))