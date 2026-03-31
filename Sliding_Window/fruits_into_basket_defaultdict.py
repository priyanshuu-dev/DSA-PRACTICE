from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        
        from collections import defaultdict
        count=defaultdict(int)
        low=0
        maximum=0

        for high in range(len(fruits)):
            count[fruits[high]]+=1

            while len(count)>2:
                count[fruits[low]]-=1

                if count[fruits[low]]==0:
                    del count[fruits[low]]
                low+=1
                    
            maximum=max(maximum,high-low+1)

        return maximum