class KthLargest:

    # constructor 
    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers 
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k : 
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # adds integer to stream and return kth largest integer in that stream 
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)  > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] 
        
