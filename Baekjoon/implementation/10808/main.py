word = input()
alp = [0]*26

for s in word :
    n = ord(s) - ord('a')
    alp[n] += 1

for i in alp :
    print(i, end=' ')