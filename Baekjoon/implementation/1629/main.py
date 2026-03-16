a, b, c = map(int, input().split())
rest = a
for _ in range(b-1):
    rest *= a
    rest %= c

print(rest)