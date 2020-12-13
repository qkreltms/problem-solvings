# 문제
'''
장르 별로 가장 많이 재생된 노래를 두 개씩 모아 고유값(index)을 출력
1. 가장 많이 재생된 노래의 장르순으로 고른다.
2. 그 장르내에서 가장 많이 재생된 노래 순으로 고른다.
3. 장그 내에서 재생 횟수가 같은 노래가 있다면 고유 번호 낮은 순으로
4. 노래가 한곡 뿐이라면 그것만 출력한다.
* 모든 장르는 재생된 횟수가 다르다 => python 정렬 함수 허용
'''
# 내 실수
'''
함수의 반환값 뭔지 파악 못 함
'''
# 키 포인트
'''
'''
# 알게된 것
'''
enumerate 에서 반환되는 값: index, values
zip 반환 => tuple
dic.items 반환 => tuple
'''

def solution(genres, plays):
    dic = {}
    sumDic = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic:
            dic[g] = [(i, p)]
        else:
            dic[g].append((i, p))
        # 장르별 재생횟수 저장
        if g not in sumDic:
            sumDic[g] = p
        else:
            sumDic[g] += p

    ans = []
    for (g, _) in sorted(sumDic.items(), key=lambda x: x[1], reverse=True):
      for (i, _) in sorted(dic[g], key=lambda x: x[1], reverse=True)[:2]:
        ans.append(i)
    return ans


print(solution(['A', 'B', 'A', 'A', 'B'], [
      500, 600, 150, 800, 2500]), [4, 1, 3, 0])
