print('123'[40:41], 'test')
def solve(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                # 문자열 왼쪽부터 오른쪽 순으로 왼쪽이 더 큰지 확인=>감소하는수
                a = int(str_num[i])
                b = int(str_num[i - 1])
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    # 11=>20, 22=>30, 33=>40
                    # 100=>110,110=>200,200=>210, 210=>220, 220=>300
                    # i-1번째가 더 작으면 +1해준 후 그 바로 뒤 0으로 만들고 나머지 앞뒤로 붙임 
                    # 이렇게하여 i-1번째가 i번째보다 무조건 작도록 만들고 그 다음 자리는 숫자가 몇이든 필요없으므로 0으로 만듦
                    # 문제는 이 방식을 어떻게 빅오로 증명??
                    start=str_num[:i - 1]
                    mid=str(int(str_num[i - 1]) + 1)
                    end='0' + str_num[i + 1:]
                    num=int(start + mid + end)
                    flag=False
                    break
        if flag:
            cnt += 1

            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1


if __name__ == "__main__":
    n=int(input())
    if n >= 1023:  # 1022: 9876543210
        print(-1)  # N번째 감소하는 수 x
    elif n == 0:
        print(0)
    else:
        print(solve(n))
