word = input()

if len(word)%2 == 0 :
    i = len(word)//2-1
    j = len(word)//2
else :
    i = len(word)//2
    j = len(word)//2

while(i>=0) :
    if (word[i] == word[j]) :
        pass
    else :
        print(0)
        exit()
    i-=1
    j+=1

print(1)