#Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
#Example 1:
#Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
#Output: 3
#Explanation: The repeated subarray with maximum length is [3,2,1].
#Example 2:
#Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
#Output: 5

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def computeKMP(pattern):
            n = len(pattern)
            lps = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]: j = lps[j - 1]
                if pattern[i] == pattern[j]: j += 1
                lps[i] = j
            return lps

        ans = 0
        while nums2:
            lps = computeKMP(nums2)
            
            j = 0  # pattern pointer
            for i in range(len(nums1)):
                while j > 0 and nums1[i] != nums2[j]: j = lps[j - 1]
                if nums1[i] == nums2[j]: j += 1
                ans = max(ans, j)
                if j == len(nums2):
                    j = lps[j-1]
            del nums2[0]
        return ans
