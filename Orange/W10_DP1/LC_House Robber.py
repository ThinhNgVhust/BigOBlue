class Solution:
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        ans = [0]*len(nums)
        ans[0] = nums[0]
        ans[1] = nums[1]
        for i in range(2,len(nums)):
            ans[i] = nums[i]+max(ans[:i-1])
        return max(ans)


sol = Solution()
print(sol.rob([1,2,3,1]))