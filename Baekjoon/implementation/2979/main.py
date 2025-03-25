a, b, c = map(int, input().split())
time = [0]*101

for _ in range(3) :
    start, end = map(int, input().split())
    for i in range(start, end) :
        time[i] += 1

money = time.count(1)*a + time.count(2)*b*2 + time.count(3)*c*3
print(money)