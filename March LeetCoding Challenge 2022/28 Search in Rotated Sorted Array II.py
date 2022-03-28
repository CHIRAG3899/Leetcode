#There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
#Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
#
#Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
#
#You must decrease the overall operation steps as much as possible.
#
# 
#
#Example 1:
#
#Input: nums = [2,5,6,0,0,1,2], target = 0
#Output: true
#Example 2:
#
#Input: nums = [2,5,6,0,0,1,2], target = 3
#Output: false

class Solution:
    def search(self, nums, target):
        def dfs(beg, end):
            if end - beg <= 1: return target in nums[beg: end+1]
            
            mid = (beg + end)//2
            if nums[mid] > nums[end]:   # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(beg, mid)
                else:
                    return dfs(mid + 1, end)
            elif nums[mid] < nums[end]: # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end)
                else:
                    return dfs(beg, mid)
            else:
                return dfs(mid+1, end) or dfs(beg, mid)
    
        return dfs(0, len(nums)-1)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return True
            
            # so that the sequence is strictly increasing or strictly decreasing
            while left < mid and nums[left] == nums[mid]:
                left += 1
            while right < mid and nums[mid] == nums[right]:
                right -= 1
            
            """
                first "if" - it is difination of the increasing sequence
                
                nums[mid] >= nums[left] - more or equal for case where mid element it is first element of array and not equal target (example nums = [3,1] target = 1)
            """
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False