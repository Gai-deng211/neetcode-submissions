class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for num in range(k):
            minimum = min(nums)
            nums[nums.index(minimum)] = minimum * multiplier
        return nums