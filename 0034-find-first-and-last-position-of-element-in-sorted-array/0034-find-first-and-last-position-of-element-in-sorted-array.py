class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        i = 0
        j = n-1
        result = [-1 , -1]

        while i <= j and nums[i] != target:
            i +=1

        while j>=i and nums[j] != target:
            j -=1 

        if i<=j:
            return [i , j]
        else: 
            return result