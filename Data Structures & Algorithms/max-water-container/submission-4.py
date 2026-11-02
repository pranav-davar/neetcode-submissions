class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## Two pointers
        l,r=0,len(heights)-1
        max_ar=0
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            max_ar=max(max_ar,area)
            if heights[l]<heights[r]:
                l+=1
            # elif heights[l]>heights[r]:
            #     r-=1
            else:
                # l+=1
                r-=1
        return max_ar