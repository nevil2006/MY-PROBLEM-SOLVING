class Solution:
    def minmax(self, arr):
        min_var = arr[0]
        max_var = arr[0]
        for i in arr:
            if i > max_var:
                max_var = i
            if i < min_var:
                min_var = i
        return [min_var, max_var]
