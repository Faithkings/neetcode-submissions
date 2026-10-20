class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq

        heap = []

        for i in nums:
            heap.append(-i)
        
        heapq.heapify(heap)

        for i in range(k):
            number = -heapq.heappop(heap)

        return number


