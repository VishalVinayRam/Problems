class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0
        total = 0 
        right =  len(height)-1
        while right >= left:
            res = min(height[left],height[right])*(right-left)
            total = max(res,total)
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        return total