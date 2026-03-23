import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
h = max(data)

sub = [0] * n

while(sum(sub) != m) :
    for i in range(n):
        s = data[i]-h
        if s > 0:
            sub[i] = s
    h -= 1

print(h+1)