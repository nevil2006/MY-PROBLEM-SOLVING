class Solution:
    def isSubset(self, a, b):
        freq = {}

        # Count frequency of each element in a[]
        for num in a:
            freq[num] = freq.get(num, 0) + 1

        # Check elements of b[] against frequency map
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1   # use one occurrence

        return True
