class solution:
        def insertAtIndex(self, arr, index, val):

            arr.append(0)
            
            i=len(arr)-1
            while i>index:
                arr[i]=arr[i-1]
                i-=1
            
            arr[index]=val
            return arr