import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(list(input().split()))

def change(array):
    return int(array[1])

result = sorted(data, key=change)

for i in result:
    print(i[0], end=' ')