class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        c=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                product*=nums[i]
            else:
                c+=1
        out = []
        for i in nums:
            match c:
                case 0:
                    out.append(product//i)
                case 1:
                    if(i==0):
                        out.append(product)
                    else:
                        out.append(0)
                case _:
                    out.append(0)
        return out