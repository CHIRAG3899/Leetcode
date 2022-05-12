#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,1,2]
#Output:
#[[1,1,2],
# [1,2,1],
# [2,1,1]]
#Example 2:
#
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        results = []
    
        def backtrack(pointer):
            if pointer == len(nums):
                results.append(nums[:])
                return
            
            seen = set() #generate an empty set eveytime the backtrack function is called
            for i in range(pointer, len(nums)):
			
                if nums[i] not in seen: #do below > if nums[i] is not already in the seen
				
                    seen.add(nums[i]) #add nums[i] to the seen so if there is a duplicate, if condition can catch it
                    
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    
                    backtrack(pointer+1)
                    
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    
        backtrack(0)
        return results