class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[r] == val:
                r -= 1
            else:
                if nums[l] == val:
                    nums[l] = nums[r]
                    nums[r] = val
                else:
                    l += 1
        return len(nums) - nums.count(val)
