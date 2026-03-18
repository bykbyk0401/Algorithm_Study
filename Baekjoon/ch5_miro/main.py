import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[0]*m for _ in range(n)]
cnt = 0
data = []

def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if x==n-1 and y==m-1:
            data.append(cnt)
            cnt=0
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y]=1
        cnt+=1
        print(cnt)
        # if x==n-1 and y==m-1:
        #     data.append(cnt)
        #     cnt=0
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x,y-1)
        
    return False


for i in range(4):
    visited = [[0]*m for _ in range(n)]
    dfs(0,j)

print(data)