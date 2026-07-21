class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [nums[i]*nums[i] for i in range(0 , len(nums))]
        nums.sort()
        return nums