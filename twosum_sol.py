# Leetcode twosum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    flag =1
                    break
                else:
                    continue
            if flag == 1:
                break
        list = [i,j]
        return list