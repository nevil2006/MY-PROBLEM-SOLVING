class solution:
    def moreFrequent(self, arr, x, y):
        countX=0
        countY=0
        for num in arr:
            if num==x:
                countX+=1
            elif num==y:
                countY+=1
        if countX>countY:
            return x
        elif countY>countX:
            return y
        else:
            return min(x,y)
