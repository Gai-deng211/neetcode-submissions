class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        l = 0 # left index
        r = 0 # right index
        T = 0 # the total index of the array

        while len(left) > l and len(nums2) > r:
            if left[l] <= nums2[r]:
                nums1[T] = left[l]
                l += 1
            else:
                nums1[T] = nums2[r]
                r += 1
            T += 1
        
        while len(left) > l:
            nums1[T] = left[l]
            T += 1
            l += 1
        while len(nums2) > r:
            nums1[T] = nums2[r]
            T += 1
            r += 1
