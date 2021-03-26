
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/\
https://m.blog.naver.com/kks227/220795165570
슬라이딩 윈도우 기법 사용
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans