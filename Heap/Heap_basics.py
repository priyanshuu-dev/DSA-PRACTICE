# #MIN HEAP
import heapq

min_heap=[]

heapq.heappush(min_heap,10)
heapq.heappush(min_heap,5)
heapq.heappush(min_heap,20)
heapq.heappush(min_heap,1)
heapq.heappush(min_heap,15)


print(min_heap)
a=heapq.heappop(min_heap)
print(a)# smallest , here 1
#pop time complexity o(log n)

#sorted order values
while min_heap:
    print(heapq.heappop(min_heap))
    # time-> n (log n )
    # n-> no of elements

#MAX HEAP
max_heap=[]

heapq.heappush(max_heap,-12)
heapq.heappush(max_heap,-30)
heapq.heappush(max_heap,-8)
heapq.heappush(max_heap,-25)
heapq.heappush(max_heap,-40)

print(max_heap)

print(-heapq.heappop(max_heap))

while max_heap:
    print(-heapq.heappop(max_heap))

