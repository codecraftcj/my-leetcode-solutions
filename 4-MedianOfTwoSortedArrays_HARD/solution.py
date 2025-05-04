class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        for num in nums1:
            nums2.append(num)
        nums2.sort()
        len_modulo_two = len(nums2) % 2

        if(len_modulo_two == 0):
            middle_number = int(len(nums2)/2)
            median = (nums2[middle_number]+nums2[middle_number-1])/2
        else:
            middle_number = floor(len(nums2)/2)
            median = nums2[middle_number]

        return median