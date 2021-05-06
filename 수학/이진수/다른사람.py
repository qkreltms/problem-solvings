#풀이 법
'''
bin 사용해 비트 길이만 파악 후 쉬프트 연산자 and 연산자 활용해 1인지 판별
'''
exec("n=int(input());print(' '.join(str(i)for i in range(len(bin(n)[2:]))if n>>i&1));"*int(input()))