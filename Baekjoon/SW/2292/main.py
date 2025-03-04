# N = int(input())

# if N==1:
#     print(1)
# else:
#     num=1
#     for i in range(1, N):
#         num+=6*i
#         if N<=num:
#             print(i+1)
#             break

num = int(input())
numbox=1
cnt=1

while num>numbox :
    numbox+=6*cnt
    cnt+=1
print(cnt)