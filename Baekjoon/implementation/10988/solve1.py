# 음수 인덱싱

word = input()
for i in range(len(word)) :
    if word[i] == word[-1-i] :
        pass
    else :
        print(0)
        exit()
print(1)