class Solution:
    ol = 0
    maxL = 1
    def longestPalindrome(self, S: str) -> str:
        self.ol = 0
        self.maxL = 1
        def p(S, j, k):
            while j>=0 and k<len(S) and S[j] == S[k]:
                j-=1
                k+=1
            if self.maxL < k-1-j:
                self.ol = j+1
                self.maxL = k-1-j
        for i in range(len(S)):
            p(S,i,i)
            p(S,i,i+1)
        return S[self.ol:self.ol+self.maxL]