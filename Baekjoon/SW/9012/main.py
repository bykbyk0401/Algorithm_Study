n = int(input())
vps = []


for _ in range(n) :
    vps.append(list(input()))

for i in range(n) :
    stack = []
    cnt = len(vps[i])
    for j in range(len(vps[i])) :
        if vps[i][j] == '(' :
            stack.append('(')
            cnt -= 1
        else :
            if len(stack) == 0 :
                print("NO")
                break
            stack.pop()
            cnt -= 1
    if len(stack) == 0 and cnt == 0 :
        print("YES")
    elif len(stack) != 0 :
        print("NO")

# T = int(input())

# for i in range(T):
#     stack = []
#     a=input()
#     for j in a:
#         if j == '(':
#             stack.append(j)
#         elif j == ')':
#             if stack:
#                 stack.pop()
#             else: # 스택에 괄호가 없을경우 NO
#                 print("NO")
#                 break
#     else: # break문으로 끊기지 않고 수행됬을경우 수행한다
#         if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#             print("YES")
#         else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#             print("NO")