import sys
input = sys.stdin.readline

x = int(input().rstrip())
data = [0]*(x+1)
cnt = 0

type = [5,3,2]
for i in type:
    k=1
    while(i*k<=x):
        data[i*k]=k
        k+=1

print(data)

while(x>1):
    if data[x] == 0:
        x-=1
    else:
        x=data[x]
    cnt += 1
    print(x)

print(cnt)