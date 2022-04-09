#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#Example 1:
#
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#Example 2:
#
#Input: nums = [1], k = 1
#Output: [1]

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:

		frequency = {}

		for num in nums:

			if num not in frequency:

				frequency[num] = 1

			else:

				frequency[num] = frequency[num] + 1

		frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

		result = list(frequency.keys())[:k]

		return result

class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]