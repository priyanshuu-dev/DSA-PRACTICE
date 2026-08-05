import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        heap=[]
        res=[]

        for i in range(len(words)):
            if words[i] in freq:
                freq[words[i]]+=1

            else:
                freq[words[i]]=1

        for word,count in freq.items():
            heapq.heappush(heap,(-count,word))

        while k:
            a,b=heapq.heappop(heap)
            res.append(b)
            k-=1

        return res