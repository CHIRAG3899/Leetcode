#In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
#If it cannot be done, return -1.
#Example 1:
#Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
#Output: 2
#Explanation: 
#The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
#If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
#Example 2:
#Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
#Output: -1
#Explanation: 
#In this case, it is not possible to rotate the dominoes to make one row of values equal.

class Solution:
    def minDominoRotations(self, A, B):
        s, n = set([1,2,3,4,5,6]), len(A)
        for i in range(n):
            s &= set([A[i], B[i]])
        if not s:
            return -1
        flips1 = sum(A[i] == list(s)[0] for i in range(n))
        flips2 = sum(B[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2)

class Solution:
	def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

		frequency_tops = {1:0,2:0,3:0,4:0,5:0,6:0}

		for i in tops:
			if i not in frequency_tops:
				frequency_tops[i] = 1
			else:
				frequency_tops[i] = frequency_tops[i] + 1

		frequency_bottoms = {1:0,2:0,3:0,4:0,5:0,6:0}

		for i in bottoms:
			if i not in frequency_bottoms:
				frequency_bottoms[i] = 1
			else:
				frequency_bottoms[i] = frequency_bottoms[i] + 1

		swap_number = 0

		for i in range(1,7):
			if frequency_tops[i] + frequency_bottoms[i] >= len(tops):
				swap_number = i

		if swap_number == 0:
			return -1

		min_num1 = len(tops)-frequency_tops[swap_number]
		min_num2 = len(bottoms)-frequency_bottoms[swap_number]


		for i in range(len(tops)):
			if swap_number not in [tops[i],bottoms[i]]:
				return -1

		return min(min_num1,min_num2)
        
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        top_fr, bot_fr, val_total = [0]*7, [0]*7, [total]*7
        for top, bot in zip(tops, bottoms):
            if top == bot:
                val_total[top] -= 1
            else:
                top_fr[top] += 1
                bot_fr[bot] += 1
                
        for val in range(1, 7):
            if (val_total[val] - top_fr[val]) == bot_fr[val]:
                return min(top_fr[val], bot_fr[val])
            
        return -1