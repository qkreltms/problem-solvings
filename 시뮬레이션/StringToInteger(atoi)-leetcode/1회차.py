#링크
'''
문제: https://leetcode.com/problems/string-to-integer-atoi/
32bit signed int를 지원하는 atoi를 만들어라
1. leading 스페이스 무시
2. 다음 문자가 있고, 그 문자가 '-', '+'인지 확인 이것이 부호가됨
3. 숫자가 아니거나 마지막이 아닐때까지 읽는다.
4. 숫자로 변환, 아무 숫자도 못 읽었다면 0으로 판단. ('00123' => 123)
5. 숫자가 -2^31 ~ 2^31-1 범위 안에 들도록함

참고:
'''
#풀이 법
'''
'''
#키포인트
'''
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        flag = 1
        if len(s) > 0:
            if s[0] == '-' or s[0] == '+':
                if s[0] == '-':
                    flag = -1
                s=s[1:]
        i=0
        while len(s)>i:
            o=ord(s[i])
            if o>=48 and o<=57:
                i+=1
            else:
                break
        
        s=flag * (0 if i == 0 else int(s[0:i])) 
            
        mp = 2**31-1
        mf = -2**31
        if s>mp:
            return mp
        elif s<mf:
            return mf
        return s