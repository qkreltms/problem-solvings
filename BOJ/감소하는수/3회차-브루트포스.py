n=int(input())
if n<=9:
    print(n)
    exit()
cnt=10
num=10
while True:
    if num > 9876543210:
        print(-1)
        exit()
    strNum=str(num)
    flag=True
    l=len(strNum)
    for i in range(l-1):
        if strNum[i]>strNum[i+1]:
            continue
        else:
            flag=False
            start=strNum[:i]
            mid=int(strNum[i])+1
            end=len(strNum[i+1:])*'0'
            num=int(f'{start}{mid}{end}')
            break
    if flag:
        if n==cnt:
            print(num)
            break
        cnt+=1
        num+=1  