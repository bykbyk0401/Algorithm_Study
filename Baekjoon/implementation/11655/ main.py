code = input().split()
new = []

for i in code :
    part = ''
    for j in i :
        if j >= 'A' and j <= 'Z' :
            part += chr(((ord(j)-ord('A') + 13) % 26) + ord('A'))
        elif j >= 'a' and j <= 'z' :
            part += chr(((ord(j)-ord('a') + 13) % 26) + ord('a'))
        else :
            part += j
    new.append(part)

print(' '.join(new))

code = input()
new = ''

for i in code :
    if i >= 'A' and i <= 'Z' :
        new += chr(((ord(i)-ord('A') + 13) % 26) + ord('A'))
    elif i >= 'a' and i <= 'z' :
        new += chr(((ord(i)-ord('a') + 13) % 26) + ord('a'))
    else :
        new += i

print(new)