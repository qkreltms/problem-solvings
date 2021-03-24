# 풀이 법
'''
배열을 순회하며 n = target - num을 진행하고
num 값을 테이블에 저장해 놓는다. h[num] = i
만약 n 값이 이미 테이블에 있는 값이라면 그 값과 현재 인덱스 값을 출력한다. 

왜냐면 예: [2, 7], 9일 때 9 - 2 = 7, 9 - 7 = 2이므로 이미 거쳐간 num 값을 저장해 놓으면 바로 답을 구할 수 있다.
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]