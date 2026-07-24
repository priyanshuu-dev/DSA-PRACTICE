class Solution:
    def isIntersect(self, intervals):
        s1=intervals[0][0]
        e1=intervals[0][1]
        
        for i in range(1,len(intervals)):
            s2=intervals[i][0]
            e2=intervals[i][1]
            
            if e1>=s2:
                return True
                
            else:
                e1=max(e1,e2)
                
        return False
                