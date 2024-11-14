from collections import deque

n, m = map(int, input().split())

miro = []

for _ in range(n):
    miro.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 상 하 좌 우 이동 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue
            if miro[nx][ny] == 1 :
                miro[nx][ny] += miro[x][y]
                queue.append((nx,ny))
            if miro[nx][ny] == 0 :
                continue

            # if문 한번에 줄여서 가능
            # if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1 :
            #     miro[nx][ny] += miro[x][y]
            #     queue.append((nx,ny))
    
    return miro[n-1][m-1]

print(bfs(0,0))