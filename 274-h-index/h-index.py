class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count_list = [0]*(n+1)

        for c in citations:
            if c > n:
                count_list[-1] += 1
            else:
                count_list[c] += 1
        
        sum = 0

        for i in range(n, -1, -1):
            sum += count_list[i]

            if sum>=i:
                return i