#Given an array of integers arr, return true if and only if it is a valid mountain array.
#Recall that arr is a mountain array if and only if:
#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#Example 1:
#Input: arr = [2,1]
#Output: false
#Example 2:
#Input: arr = [3,5,5]
#Output: false
#Example 3:
#Input: arr = [0,3,2,1]
#Output: true

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        checked = False # Variable used to check the summit of the mountain 
        if len(arr) < 3 or arr[0] > arr[1]: # Pre-conditions , if the len(arr) < 3 or if arr[0] > arr[1] meaning that we're decreasing from the beginning which is not allowed
            return False
        for i in range(len(arr)-1): # Iterate through the array 
            if not checked and not arr[i] < arr[i+1]: # Check for the summit of the mountain and if we're increasing
                checked = True
            if checked and not (arr[i] > arr[i+1]): # Check if after the summit we're decreasing
                return False
            if not checked and i == len(arr)-2: # Check if the array only increase
                return False
        return True
