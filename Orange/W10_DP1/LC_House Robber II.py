class Solution:
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        n = len(nums)
        arr1 = nums[:n-1]
        arr2 = nums[1:]
        ans1 = [0] * len(arr1)
        ans1[0] = arr1[0]
        ans1[1] = arr1[1]
        for i in range(2, len(arr1)):
            ans1[i] = arr1[i] + max(ans1[:i - 1])


        ans2 = [0] * len(arr2)
        ans2[0] = arr2[0]
        ans2[1] = arr2[1]
        for i in range(2, len(arr2)):
            ans2[i] = arr2[i] + max(ans2[:i - 1])
        return max(max(ans1),max(ans2))