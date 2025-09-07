class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s) # frequency hash table with highest freq first 
        maxheap = []
        for key in freq.keys():
            heapq.heappush(maxheap, (-freq[key], key))
        result = ""
        prev_char = ''
        prev_count = 0
        while maxheap:
            count, char = heapq.heappop(maxheap)
            if prev_count < 0: # must push to heap for previous now because if we push right when iterating previous, it could result in time exceeded
                heapq.heappush(maxheap, (prev_count, prev_char))
            if char != prev_char:
                result += char
                count += 1
                prev_count = count
                prev_char = char
        if len(result) != len(s): # must be same length
            return ""
        else:
            return result