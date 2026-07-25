class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        start.sort()
        end.sort()
        count=0
        
        i=0
        j=0
        
        answer=0
        
        while i<len(start) and j<len(end):
            
            if start[i]<end[j]:
                count+=1
                i+=1
                
                answer=max(count,answer)
                
            else:
                count-=1
                j+=1
                
        return answer