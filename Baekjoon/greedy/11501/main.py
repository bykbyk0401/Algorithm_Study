import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    days = int(input())
    stock = list(map(int, input().split(' ')))
    result = 0
    j = 0

    for i in range(len(stock)-1):
        if i == len(stock)-2 and stock[i] <= stock[i+1]:
            result += stock[i+1] - stock[i]
            break
        if stock[i] <= stock[i+1] :
            continue
        for _ in range(j,i+1) :
            result += stock[i]-stock[j]
            j+=1
    print(result)