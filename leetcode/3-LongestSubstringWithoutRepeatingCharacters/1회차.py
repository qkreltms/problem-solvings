'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set([0])
        S = list(s)
        if len(S) == 1:
            return 1
        for i in range(1, len(S)):
            p = []
            for j in range(i, len(S)):
                p.append(S[j-1])
                next = S[j]
                if next in p:
                    ans.add(len(p))
                    break
                if len(S)-1 == j:
                    p.append(next)
                    ans.add(len(p))
        return max(ans)


print(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
print(Solution().lengthOfLongestSubstring('bbbbb'), 1)
print(Solution().lengthOfLongestSubstring('pwwkew'), 3)
print(Solution().lengthOfLongestSubstring(''), 0)
print(Solution().lengthOfLongestSubstring('1'), 1)
print(Solution().lengthOfLongestSubstring('12'), 2)
print(Solution().lengthOfLongestSubstring('!@#123!'), 6)
print(Solution().lengthOfLongestSubstring('dvdf'), 3)
