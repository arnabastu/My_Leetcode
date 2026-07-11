class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_pov = []
        nums_neg = []
        result = []

        for i in range(0 , n):
            if nums[i] > 0:
                nums_pov.append(nums[i])
            else:
                nums_neg.append(nums[i])
        
        for j in range(0 , len(nums_pov)):
            result.append(nums_pov[j])
            result.append(nums_neg[j])

        return result