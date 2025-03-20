
init = list(input())
y = init[0]
x = int(init[1])
cnt = 0

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(alp)) :
    if y == alp[i] :
        y = i+1

if x-2 > 0 and x-2 < 9 :
    if y-1 > 0 and y-1 < 9 :
        cnt += 1
    if y+1 > 0 and y+1 < 9 :
        cnt += 1
if y+2 > 0 and y+2 < 9 :
    if x-1 > 0 and x-1 < 9 :
        cnt += 1
    if x+1 > 0 and x+1 < 9 :
        cnt += 1
if x+2 > 0 and x+2 < 9 :
    if y-1 > 0 and y-1 < 9 :
        cnt += 1
    if y+1 > 0 and y+1 < 9 :
        cnt += 1
if y-2 > 0 and y-2 < 9 :
    if x-1 > 0 and x-1 < 9 :
        cnt += 1
    if x+1 > 0 and x+1 < 9 :
        cnt += 1

print(cnt)