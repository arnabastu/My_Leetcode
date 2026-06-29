class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        i = 0
        j = n -1

        while i<=j:
            mid = i + (j - i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i