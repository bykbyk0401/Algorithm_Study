height = []
for _ in range(9) :
    height.append(int(input()))

height.sort()

for i in range(8) :
    for j in range(i+1, 9) :
        two = height[i]+height[j]
        if sum(height) - two == 100 :
            for k in range(9) :
                if k == i or k == j :
                    pass
                else :
                    print(height[k])
            exit()