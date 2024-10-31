n = input()
lst = [0 for _ in range(26)]
#[0]을 총 26개로 초기화
#lst = [0]*26 


for i in n:
    lst[ord(i)-ord('a')] += 1
    # ord(문자) = 숫자 ; 문자를 숫자로 바꿔주는 함수
    
for i in lst:
    print(i, end=' ')