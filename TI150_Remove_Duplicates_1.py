class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        uniq = 1
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                for j in range(i+1, len(nums)):
                    if nums[j] > prev:
                        nums[i] = nums[j]
                        prev = nums[i]
                        uniq += 1
                        break
            else:
                prev = nums[i]
                uniq += 1
        return uniq
