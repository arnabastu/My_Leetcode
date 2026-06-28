class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = nums1 + nums2 
        merge.sort()

        n = len(merge)

        if n % 2 == 1:
            
            return float(merge[n // 2])
        else:
            
            val1 = merge[(n // 2) - 1]
            val2 = merge[n // 2]
            return (val1 + val2) / 2.0