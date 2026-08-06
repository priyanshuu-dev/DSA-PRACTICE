#leetcode 767
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1

            else:
                freq[s[i]]=1
        heap=[]
  
        for char,count in freq.items():
            heapq.heappush(heap,(-count,char))

        ans=""
        
        while heap:
            num,val=heapq.heappop(heap)
            num=num*(-1)

            if len(ans)==0:
                ans+=val
                num-=1

                if num>0:
                    heapq.heappush(heap,(-num,val))
            
            elif val!=ans[-1]:
                ans+=val
                num-=1

                if num>0:
                    heapq.heappush(heap,(-num,val))

            else:
                if not heap:
                    return ""
                
                num2,val2=heapq.heappop(heap)
                num2=num2*(-1)


                ans+=val2
                num2-=1

                if num2>0:
                    heapq.heappush(heap,(-num2,val2))

                heapq.heappush(heap,(-num,val))

        if len(ans)==len(s):
            return ans

        else:
            return ""