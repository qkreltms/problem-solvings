'''
'''
class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
      h = {}
      ans = 0
      i = 0
      for j in range(len(S)):
        if S[j] in h:
          # 예를 들어 abba 일 때 "max가 없으면" j = 3일 때 i가 0으로 돌아가 잘 못 된값 3이 나온다.
          i = max(i, h[S[j]])
        ans = max(ans, j-i+1)
        h[S[j]] = j+1
      return ans


print(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
print(Solution().lengthOfLongestSubstring(''), 0)
print(Solution().lengthOfLongestSubstring('1'), 1)
print(Solution().lengthOfLongestSubstring('abcdef'), 6)