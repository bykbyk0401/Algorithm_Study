import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_list = []

for _ in range(n):
    arr = list(map(int, input().split()))
    min_list.append(min(arr))

print(max(min_list))