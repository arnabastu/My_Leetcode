class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        n_sum = (n*(n+1))/2
        nums_sum = 0

        for i in range(0 , n):
            nums_sum += nums[i]

        missing_num = n_sum - nums_sum
        return missing_num



