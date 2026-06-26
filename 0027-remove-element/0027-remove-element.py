class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count+=1
        return count
        