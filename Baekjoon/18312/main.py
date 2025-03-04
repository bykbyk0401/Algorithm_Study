# 완전탐색

N, K = map(int, input().split())
K = str(K)

cnt=0

for i in range(N+1) :
    for j in range(60) :
        for k in range(60) :
            if K in str(i)+str(j)+str(k) :
                cnt+=1

print(cnt)