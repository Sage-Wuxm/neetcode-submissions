class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        for num in nums: 
            if num != val: 
                new_nums.append(num)
        i = 0
        j = 0 
        for i in range(len(new_nums)):
            nums[j] = new_nums[j] 
            j += 1
        return len(new_nums)