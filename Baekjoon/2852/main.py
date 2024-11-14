n=int(input())

one_time=0 #1번팀이 이기는 시간
two_time=0
flag=0
for i in range(n):
    team, time=input().split()
    m,s=map(int, time.split(':'))
    if team=='1':
        if flag==0:
            one_time+=48*60-(60*m+s)
        flag+=1
        if flag==0:
            if two_time>0:
                two_time=two_time-(48*60-(60*m+s))
    else: 
        if flag==0:
            two_time+=48*60-(60*m+s)
        flag-=1
        if flag==0: #비김
            if one_time>0:
                one_time=one_time-(48*60-(60*m+s))

        
print('{:0>2}:{:0>2}'.format(one_time//60,one_time%60))
print('{:0>2}:{:0>2}'.format(two_time//60,two_time%60))
#끝났을 때 무승부