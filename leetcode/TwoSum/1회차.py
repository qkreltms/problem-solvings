'''
https://leetcode.com/problems/two-sum/
숫자 배열과 타겟이 주어질 때
이 배열안의 2개 값으로 타겟이 되는 그 2개 값의 인덱스를 출력하라
'''
def f(nums, target):
  for i in  range(0, len(nums)):
    for j in range(i, len(nums)):
      if i == j:
        continue
      if (nums[i] + nums[j]) == target:
        return [i, j]

print(f([2,7,11,15], 9))
print(f([3,2,4], 6))
print(f([3,3], 6))
print(f([3,2,3], 6))
