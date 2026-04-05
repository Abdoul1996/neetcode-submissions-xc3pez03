class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # step 1: Prefix 
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # step 2: Suffix
        suffix = 1
        for i in range(n-1, -1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        return output 

        