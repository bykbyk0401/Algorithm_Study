# 시뮬레이션

# n = int(input())
# way = input().split()

# x=1
# y=1

# for i in way :
#     # if x == 0 :
#     #     x += 1
#     #     continue
#     # elif x > n :
#     #     x 
#     #     continue
#     # elif y == 0 or y > n :
#     #     continue

#     if i == 'R' :
#         if y == n :
#             continue
#         y += 1
#     elif i == 'L' :
#         if y == 1 :
#             continue
#         y -= 1
#     elif i == 'U' :
#         if x == 1 :
#             continue
#         x -= 1
#     elif i == 'D' :
#         if x == n :
#             continue
#         x += 1

# print(x, y)

n = int(input())
x, y = 1, 1
ways = input().split()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'U', 'D']

for way in ways :
    for i in range(len(move_types)) :
        if way == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny > n :
            continue
        x = nx
        y = ny

print(x, y)