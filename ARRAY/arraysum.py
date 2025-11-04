class Solution:
    def arraySum(self, arr):
        total = 0                  # Step 1: Start with sum = 0
        for num in arr:            # Step 2: Loop through each element
            total += num           # Step 3: Add element to total
        return (total)               # Step 4: Print the sum
