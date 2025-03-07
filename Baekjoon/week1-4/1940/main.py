n = int(input())
m = int(input())
nums = list(map(int,input().split()))

# Two pointers 알고리즘 이용
nums.sort()
left, right = 0, len(nums) - 1
count = 0

while left < right:
    sum_num = nums[left] + nums[right]
    if sum_num < m:
        left += 1
    elif sum_num > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)