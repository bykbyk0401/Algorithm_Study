name = list(input())
name.sort()
mid = ''

# 팰린드롬 가능 여부
if len(name)%2 == 0 :
    for i in name :
        if name.count(i)%2 == 1 :
            print("I'm Sorry Hansoo")
            exit()
else :
    odd = 0
    for i in name :
        if name.count(i)%2 == 1 :
            odd += 1
            mid = i
    if odd%2 == 0 :
        print("I'm Sorry Hansoo")
        exit()


# 팰린드롬 만들기
n = len(name)
new = ['']*n
if mid != '' :
    name.remove(mid)

for i in range(n//2) :
    if name[i] != name[i+1] :
        continue
    new[i] = name[i]
    new[n-i-1] = name[i]
    i+=2

print(new)