T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됐을경우 수행
        if not stack:
            print("YES")
        else:
            print("NO")