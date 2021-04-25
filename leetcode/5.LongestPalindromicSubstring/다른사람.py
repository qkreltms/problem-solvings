# 링크
'''
문제:
참고: https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
'''
# 풀이 법
'''
'''
# 키포인트
'''
'''


class Solution1(object):

    def __init__(self):
        self.lo = 0
        # 0보다 1로하면 속도가 더 빨리짐 왜?
        self.maxlen = 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            self.__extendPalindrome(s, i, i) # 홀수
            self.__extendPalindrome(s, i, i+1) # 짝수
        return s[self.lo: self.lo + self.maxlen]

    def __extendPalindrome(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            # 최대 길이를 구하는 것이므로 최대 길이 넘는 것만
        if self.maxlen < right -1 - left:
            self.lo = left + 1  # left+1:  our l-- will go  unequal OR off bounds
            # 만약 addbab, i=4, l=2, r=6 일 때 r이 한칸 더 넘어갔으므로 -1해주고 l만큼의 공간을 r에서 빼면 
            # 길이 값이 나온다.  
            self.maxlen = right -1 - left # right-1:  our r++ will go  unequal OR off bounds, python에 맞춘 식


# Solution1().longestPalindrome('babad')
# print(Solution1().longestPalindrome('abefba'))
print(Solution1().longestPalindrome('cbabd'))
# print(Solution1().longestPalindrome('babad'))
# print(Solution1().longestPalindrome('adbab'))
