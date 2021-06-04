class Solution:
    le=0
    gl,gr=0,0
    def longestPalindrome(self, s: str) -> str:
        def f(l,r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            if r-l-1>self.le:
                self.le=r-l-1
                self.gl=l+1
                self.gr=r-1
        for c in range(len(s)):
            f(c,c)
            f(c,c+1)
        return s[self.gl:self.gr+1]