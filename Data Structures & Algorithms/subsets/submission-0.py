class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path.copy())

            for i in range(start, len(nums)):
                # chose 
                path.append(nums[i])

                # Recurse (move forward)
                backtrack(i+1)

                path.pop()
        backtrack(0)
        return res
        