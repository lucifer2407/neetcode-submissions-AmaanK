class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for i,num in enumerate(nums):
            if num not in num_map:
                num_map[num] = i
            else:
                return True
        return False

