import itertools

height = [int(input()) for _ in range(9)]

for i in itertools.combinations(height, 7) : # 해당 배열 7명 중복없이 뽑아줌
    if sum(i) == 100 :
        for j in sorted(i) :
            print(j)
        break