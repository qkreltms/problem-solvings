'''
https://leetcode.com/problems/palindrome-number/

숫자가 주어졌을 때
거꾸로 뒤집어도 순서가 같을 때
'''
# 배운 점
'''
xs[3:0:-1] # 0번 인덱스부터 3번 인덱스까지 역순 출력
xs[0:3] # 0번 인덱스부터 3번 인덱스까지 출력
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
      xs = str(x)
      # NOTE: 가운데부터 뒤집는게 더 성능 up! 할 수 있음
      if xs == xs[::-1]:
        return True
      return False

print(Solution().isPalindrome(-121), False)
print(Solution().isPalindrome(121), True)