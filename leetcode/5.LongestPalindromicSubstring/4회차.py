class Solution:
    def __init__(self):
        self.ol = 0
        self.maxL = 1
    def longestPalindrome(self, s: str) -> str:

        def f(s, j, k):
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            if self.maxL < - j + k - 1:
                self.ol = j + 1
                self.maxL = - j + k - 1 
            
        for i in range(len(s)):
            f(s, i, i)
            f(s, i, i+1)
        return s[self.ol:self.maxL+self.ol]
