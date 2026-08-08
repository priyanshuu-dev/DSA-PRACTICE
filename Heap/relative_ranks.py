import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[]
        for index,num in enumerate(score):
            heapq.heappush(heap,(-num,index))

        if heap:
            a1,b1=heapq.heappop(heap)
            score[b1]="Gold Medal"

        if heap:
            a2,b2=heapq.heappop(heap)
            score[b2]="Silver Medal"

        if heap:
            a3,b3=heapq.heappop(heap)
            score[b3]="Bronze Medal"

        rank=4

        while heap:
            a,b=heapq.heappop(heap)
            score[b]=str(rank)

            rank+=1

        return score