'''
'''
# 고려사항
'''
음수 값,
같은 값
'''
# 배운 점
'''
손코딩으로 100% 구현하고 해보자
'''

from typing import List
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash = {}
    for i, n in enumerate(nums):
      x = target - n
      if x in hash:
        return [hash[x], i]
      hash[n] = i 

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))
print(Solution().twoSum([3,2,3], 6))