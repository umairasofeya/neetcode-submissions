class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = [] 

        for i in range(len(nums)): 
            if nums[i] in ans: 
                return True 
            ans.append(nums[i])
        
        return False


