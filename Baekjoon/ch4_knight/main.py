import sys
input = sys.stdin.readline

data = input().split()

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x=0
y=int(data[1])

for i in range(len(alp)) :
    if alp[i] == data[0] :
        y = i+1

for j in range(4) :
    if j == 0 or j == 1 :
        nx = x-1

# twodx = [0, 0, -2, 2]
# twody = [2, -2, 0, 0]
# onedx = [0, 0, ]