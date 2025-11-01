class Solution:
    def largest(self, arr):
        largest = arr[0]                     
        for current_element in arr:          
            if current_element > largest:  
                largest = current_element
        return largest                       