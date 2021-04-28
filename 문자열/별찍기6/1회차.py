n = int(input())
for i in range(n-1, -1, -1):
    print(f"{' '*(n-i-1)}{'*'*(i*2+1)}")