import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        
        if not scoville:
            return -1
        
        second = heapq.heappop(scoville)
        
        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        
        count += 1
    
    return count