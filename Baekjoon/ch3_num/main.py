import sys
input = sys.stdin.readline

n,m,k = map(int, input( ).split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
result = 0
i = k

for _ in range(m):
    if i == 0 :
        result+=nums[1]
        i = k
        continue
    result+=nums[0]
    i-=1

print(result)