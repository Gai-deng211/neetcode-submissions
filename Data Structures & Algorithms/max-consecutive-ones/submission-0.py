class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        highest_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                if highest_streak < current_streak:
                    highest_streak = current_streak
                current_streak = 0
        # last group
        if highest_streak < current_streak:
            highest_streak = current_streak

        return highest_streak
