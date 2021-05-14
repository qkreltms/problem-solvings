# 링크: https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-1062-%EA%B0%80%EB%A5%B4%EC%B9%A8
# 풀이 법
'''
문제는 결국 k개의 알파벳을 배워서 몇 개의 단어를 읽을 수 있는지 표시하는 것이므로
k개의 알파벳 조합 (a,b,c,d,e), (a,b,c,d,f),... 와 같은 조합을 만든 후 순회하면서 
word를 읽을 수 있는지 판별한다.
'''
from sys import stdin
from itertools import combinations
from string import ascii_lowercase


n, k = map(int, stdin.readline().split())
words = []
# 각 입력 단어에 대하여
# 1. 앞의 anta와 뒤의 tica를 슬라이스한 뒤 set로 만들고
# 2. 그중 a/c/i/t/n을 제외한 뒤 words 리스트에 저장, 만약 a,c,i,t,n 으로 이루어져있다면 공집합
for _ in range(n):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n'))

# a/c/i/t/n을 제외한 알파벳 모음
except_acitn = set(ascii_lowercase).difference('a', 'c', 'i', 't', 'n')
max_count = 0

if k < 5:
    print(0)

else:
    test = list(combinations(except_acitn, k - 5))
    for x in list(combinations(except_acitn, k - 5)):
        count = 0
        for word in words:
            # note: 
            # set([1])-set([1,2]) = set()
            # set([])-set([1,2]) = set()
            # set([3])-set([1,2]) = {3}
            # 차집합은 A-B일 때 A에서 B의 원소를 제거한다.
            if not word.difference(x):
                count += 1

        max_count = max(max_count, count)

    print(max_count)