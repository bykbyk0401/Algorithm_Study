n = int(input())
m = int(input())

num = input().split(' ')
cnt=0

for i in range(n-1) :
    for j in range(i+1, n) :
        if int(num[i])+int(num[j]) == m :
            cnt+=1

print(cnt)