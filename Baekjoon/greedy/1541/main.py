import sys
input = sys.stdin.readline

bun = input().split('-')
result = 0
for i in bun :
    add = i.split('+')
    sum = 0
    for j in add :
        sum += int(j)

    if i == bun[0] :
        result += sum
    else : 
        result -= sum

print(result)