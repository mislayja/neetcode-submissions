class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        
        total = 0
        for idx in range(len(heights)):
            if sorted_heights[idx] !=heights[idx]:
                total+=1

        return total