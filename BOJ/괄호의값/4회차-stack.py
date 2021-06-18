q=input()
s=[]
for t in q:
    if t==')':
        cnt=0
        # 항시 s 비었는지 확인 필요
        if not s:
            print(0)
            exit()
        # 3회차에서는 True로 ']'를 걸러낼 수 있지만, 여기서는 못 걸러넴
        while s:
            st=s.pop()
            if st=='(':
                if cnt>0:
                    cnt*=2
                    s.append(cnt)
                else:
                    s.append(2)
                break
            # 항시 s 비었는지 확인 필요
            elif not s or st=='[' or st==']':
                print(0)
                exit()
            else:
                cnt+=st
    elif t==']':
        cnt=0
        if not s:
            print(0)
            exit()
        while s:
            st=s.pop()
            if st=='[':
                if cnt>0:
                    cnt*=3
                    s.append(cnt)
                else:
                    s.append(3)
                break
            elif not s or st=='(' or st==')':
                print(0)
                exit()
            else:
                cnt+=st
    else:
        s.append(t)
ans=0
for i in s:
    if not isinstance(i, int):
        print(0)
        exit()
    ans+=i
print(ans)
        