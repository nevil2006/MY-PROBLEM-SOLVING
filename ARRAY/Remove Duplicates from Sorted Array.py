class Solution:
    def removeDuplicates(self, nums):
        nums.sort()  

        if not nums:
            return 0
        
        k = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # move unique element to position k
                k += 1
        
        return k  # new length of unique elements

# Example 1
nums = [1, 1, 2]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 2
