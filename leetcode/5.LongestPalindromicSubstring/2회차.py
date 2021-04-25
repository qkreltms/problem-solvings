# 링크
'''
문제:
참고: https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
'''
# 풀이 법
'''
문자열이 주어지면 0번째부터 문자열 n번째 끝까지 순회하면서
문자열의 (n번째), (n번째, n+1번째)의 문자 양 옆(r, l)이 같은지 확인한다.
같다면 팰린드롬이므로 그 길이(- l + r - 1)가 이전 최대값이랑 비교해서 큰지 확인한다. 크다면 찾은 값이 젤 긴 팰린드롬이다.
'''
# 키포인트
'''
현재 문자, 문자열의 양옆을 확인하며 팰린드롬을 찾는다.
'''
class Solution(object):
    ol = 0
    maxL = 1
    def p(self, S, l, r):
        # 인덱스 범위를 초과하지 않는 선에서 팰린드롬의 위치를 찾는다.
        while l >= 0 and r < len(S) and S[l] == S[r]:
            # 양 옆으로 이동한다.
            l-=1; r+=1
        # 이전 최대 길이를 초과하는가?
        if self.maxL < r-1-l:
            self.ol = l+1 # 앞에서 l에 추가된 1만큼의 길이를 감소해준다.
            self.maxL = r-1-l # 앞에서 r에 추가된 1만큼의 길이를 감소해주고 왼쪽 만큼의 길이를 감소해주면 길이가 나온다.
        
    def longestPalindrome(self, S):
        for i in range(len(S)):
            self.p(S, i, i+1) # 문자열 길이가 짝수 일때
            self.p(S, i, i) # 문자열이 길이가 홀수 일때
        # 가장긴 팰린드롬을 반환한다.
        return S[self.ol:self.ol+self.maxL]
