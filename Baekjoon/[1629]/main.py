# a,b,c = map(int,input().split())
# mult = 1

# for _ in range(b):
#     mult*=a

# print(mult%c)
### 시간초과 --------------------------------------

a,b,c = map(int,input().split())

def multi (a,n):
    if n == 1:
        return a%c
    else:
        tmp = multi(a,n//2)
        if n %2 ==0:
            return (tmp * tmp) % c
        else:
            return (tmp  * tmp *a) %c
            
print(multi(a,b))