class solution:
    def getAlternative(self, arr):
        result=[] 
        for i in range(len(arr)):
            if i%2==0:
                result.append(arr[i])
        return result