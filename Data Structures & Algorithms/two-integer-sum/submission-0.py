class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_seen = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in comp_seen:
                return [comp_seen[comp],i]
            comp_seen[nums[i]] = i
