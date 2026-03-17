import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

map = []
for _ in range(n):
    map.append(input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
map[x][y] = '1'
result = 1
cnt = 0

while(True):
    d = (d-1) % 4
    nx = x + dx[d]
    ny = y + dy[d]

    if map[nx][ny] == '0':
        map[nx][ny] = '1'
        result += 1
        x = nx
        y = ny
        cnt = 0
    else:
        cnt+=1

    if cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if map[nx][ny] == '1':
            break

        x = nx
        y = ny
        result += 1
        cnt = 0

print(result)