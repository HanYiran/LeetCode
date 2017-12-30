import heapq
# def heapq_int():
#     heap = []
#     heapq.heappush(heap,10)
#     heapq.heappush(heap,1)
#     heapq.heappush(heap,10/2)
#     [heapq.heappush(heap,i) for i in range(10)]
#     [heapq.heappush(heap,10-i) for i in range(10)]
#
#     print(heapq.nlargest(10,heap))
#     print([heapq.heappop(heap) for i in range(len(heap))])


def heapq_int():
    heap = []
    heapq.heappush(heap,(10,'ten'))
    heapq.heappush(heap,(1,'one'))
    heapq.heappush(heap,(10/2,'five'))
    while heap:
        print(heapq.heappop(heap))
    print()
heapq_int()