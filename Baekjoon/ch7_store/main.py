import sys
input = sys.stdin.readline

n = int(input())
store = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

store.sort()

def search(s,e,t,a):
    if s>e:
        return "no"
    m = (s+e)//2
    if a[m] == t:
        return "yes"
    elif a[m]<t :
        return search(m+1,e,t,a)
    elif a[m]>t :
        return search(s,m-1,t,a)

for i in find:
    print(search(0,n-1,i,store), end=' ')