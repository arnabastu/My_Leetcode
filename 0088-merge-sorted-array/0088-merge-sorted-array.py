class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        for i in range(0 , m):
            result.append(nums1[i])
        for j in range(0 , n):
            result.append(nums2[j])
        result.sort()
        nums1[:] = result
        