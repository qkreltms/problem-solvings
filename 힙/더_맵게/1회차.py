#문제
'''
return 섞어야 하는 최소 횟수, 단 K 이상
만들 수 없으면 -1 => 
1. 스코빌 배열이 한 칸씩 줄어드는데 조건을 못 충족시키고 더이상 없을 때, 
2. 두 번째 작은 값이 0 일 때


음식 스코빌 지수가 든 배열이 들어오고
모든 음식의 지수를 K 이상으로 만들고 싶다.
그래서 가장 낮은 두 개의 음식 F를
F + (두 번째로 맵지 않은 음식 지수 * 2)로
새로운 음식을 만든다.
모든 음식이 K 이상이 될 때까지 섞는다.

'''
#키 포인트
'''
힙을 사용해 성능을 낮춰야한다.

scov 배열 길이가 1개일 때도 확인 해야 한다.
'''
def solution(scov, k):
  cnt = 0
  while scov:
    flag = True
    for i in scov:
      if i < k:
        flag = False
        break
    if flag:
      return cnt
    if len(scov) < 2:
      if scov[0] < k:
        return -1
      return cnt
    a = min(scov)
    scov.remove(a)
    b = min(scov)
    scov.remove(b)
    c = a + b * 2
    cnt += 1
    scov.append(c)
  
  return -1

print(solution([1,2,3,9,10,12], 7), 2)
print(solution([0,2,3,9,10,12], 7), 2)
print(solution([0,0,3,9,10,12], 7), 3)
print(solution([0,0,0,0], 7), -1)
print(solution([0,0,3,9,10,12], 7000), -1)
print(solution([0,0,3,9,10,12], 0), 0)
print(solution([0,0,3,9,10,12], 1), 2)
print(solution([0,0], 0), 0)
print(solution([0,0], 1), -1)
print(solution([1,0], 1), 1)


