class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()