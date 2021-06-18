n=int(input())
if n == 0:
    print(0)
    exit()
cnt=1
num=1
while True:
    if num>9876543210:
        print(-1)
        break
    strNum=str(num)
    l=len(strNum)
    flag=True
    if l>1:
        for i in range(l-1):
            if strNum[i]>strNum[i+1]:
                continue
            else:
                start=strNum[:i]
                mid=int(strNum[i])+1
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
    