class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in index_of:
                return [index_of[need], i]
            index_of[x] = i
        return []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        