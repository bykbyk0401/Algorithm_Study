n = int(input())
pattern = input().split('*')
answer = []
for _ in range(n) :
    s = input()

    if len(s) < len(pattern[0]) + len(pattern[1]):
        answer.append('NE')
        continue

    start=0
    end=len(s)-len(pattern[1])
    stop=False
    if not stop :
        for i in pattern[0] :
            if s[start] == i :
                pass
            else :
                answer.append('NE')
                stop=True
                break
            start+=1
    if not stop :
        for i in pattern[1] :
            if s[end] == i :
                pass
            else :
                answer.append('NE')
                stop=True
                break
            end+=1
    if not stop :
        answer.append('DA')


for i in answer :
    print(i)