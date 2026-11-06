class Solution:
    def maxArea(self, height: List[int]) -> int:
        # isnt this classic 2 pointer? 
        # start left and right
        # track max
        # move left or right looking for larger value
        l = 0
        r = len(height)-1
        m = min(height[l], height[r])*(r-l)

        while l<r:
            m = max(m, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return m
        