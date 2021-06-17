#링크
'''
문제: https://www.acmicpc.net/problem/1038
참고:

감소하는 수 = 1,2,3,4,5,6,7,8,9,10,20,21,30,31,32,40,41,42,43,50,51,52,53,54,...
자연수 1,2,3,...무한 집합이 있고 1부터 무한까지 순회할 때 주어지는 감소하는 수 n에 맞는 자연수는?
예 n=18 자연수=42
'''
#풀이 법
'''
자연수 집합을 순회하며 각 자릿수가 앞자리수보다 작은지 확인한다. 모두 True라면 => 감소하는 수
아니라면 점프한다.
예를 들어 11이 나올 때 12,13,..,19까지는 필요없으므로 20으로 점프. 10의 자리, 100의자리, 1000의 자리, ..., n자리 점프
'''
#키포인트
'''
10^n자리 수 점프뛰기
'''

n=int(input())
num=1
cnt=1
if n == 0:
    print(0)
    exit()
while True:
    if num>9876543210: # 이 수보다 더 높이 가면 더 이상 감소수가 아니다.
        print(-1)
        break
    strNum=str(num)
    l=len(strNum)
    flag=True
    if l>1:
        for i in range(0,l-1):
            # 앞자리가 더 크면 감소수 이므로 다음 자릿수 구함
            if strNum[i]>strNum[i+1]:
                continue
            else:
                # 점프를 뛴다.
                # 예를 들어 11이 나올 때 12,13,..,19까지는 필요없으므로 20으로 점프. 10의 자리, 100의자리, 1000의 자리, ..., n자리 점프
                start=strNum[:i]
                mid=int(strNum[i])+1
                # 뒷자리를 전부 0으로 만든다.
                # 왜냐면, 예를 들어 num=4221일 때 4300, 4301=>4310, 4311=>4320으로 만드는게 더 깔끔함
                end=len(strNum[i+1:])*'0'
                num=int(f'{start}{mid}{end}')
                flag=False
                break
    if flag:
        if cnt==n:
            print(num)
            break
        cnt+=1
        num+=1