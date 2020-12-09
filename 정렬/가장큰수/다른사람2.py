import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    print(a,b,t1,t2) 
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0 // 1이면 a가 왼쪽 이동, -1이면 b가 왼쪽 이동

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 11]))