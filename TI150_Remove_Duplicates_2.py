class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        prevEnc = False
        ret = len(nums)
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                ret -= 1
        for i in range(1, len(nums)):
            #print(nums)
            if nums[i] == prev:
                if not prevEnc:
                    prevEnc = True
                else:
                    for j in range(i+1, len(nums)):
                        if nums[j] > prev:
                            nums[i] = nums[j]
                            nums[j] = prev
                            prev = nums[i]
                            prevEnc = False
                            break
            elif nums[i] < prev:
                for j in range(i+1, len(nums)):
                    if nums[j] >= prev:
                        if nums[j] == prev:
                            if prevEnc:
                                continue
                            else:
                                prevEnc = True
                        else:
                            prev = nums[j]
                            prevEnc = False
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
            else:
                prev = nums[i]
                prevEnc = False
        #print(nums)
        return ret
