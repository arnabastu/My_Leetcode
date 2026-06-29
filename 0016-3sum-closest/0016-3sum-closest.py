class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(n - 2):
            j = i +1 
            k = n -1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum == target:
                    return target
                if abs(total_sum - target) < abs(closest_sum -target):
                    closest_sum = total_sum
                if total_sum < target:
                    j += 1
                else: 
                    k-= 1
        return closest_sum
        