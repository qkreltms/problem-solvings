
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/\
https://m.blog.naver.com/kks227/220795165570
슬라이딩 윈도우 기법 사용


j는 계속 앞으로 이동하고
i는 이미 map에 들어있는 문자가 있다면 그 때의 j 인덱스로 이동
이렇게 하면서 ans = max(ans, j-i+1) 값을 계속 구함
i와 j는 계속 증가해야한다.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                # i 값이 뒤로 돌아가지 않도록 해줌
                i = max(mp[s[j]], i)

            # 아래 두 라인에 1을 더해준 이유는 문자열이 최소 1개는 들어오고 종료되므로
            # 이전에 찾은 문자열 위치, 현재 문자열 위치를 빼서 간격을 구한다.
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

print(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
