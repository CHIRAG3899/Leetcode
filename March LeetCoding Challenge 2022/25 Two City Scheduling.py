#A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
#Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
#Example 1:
##Input: costs = [[10,20],[30,200],[400,50],[30,20]]
#Output: 110
#Explanation: 
#The first person goes to city A for a cost of 10.
#The second person goes to city A for a cost of 30.
#The third person goes to city B for a cost of 50.
#The fourth person goes to city B for a cost of 20.
#The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
#Example 2:
#Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
##Output: 1859
#Example 3:
#Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
#Output: 3086


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # If all the people travels to the cityA then total cost:
        totalA = 0
        for costA, _ in costs:
            totalA += costA
        
        # If all the people wish to travel to cityB instead of cityA then the difference in cost would be:
        difference = [costB-costA for costA, costB in costs]
        
        """
            Since in both the cities the number of people travelling should be equal and their total cost should be minimum,
            So if we move half of the people from cityA to cityB having minimum difference among all the people then the total cost would be the minimum.
        """
        # Total cost of people travelling to cityB instead of cityA having minimum difference:
        totalB = sum(sorted(difference)[:len(costs)//2])
		
		# Total cost of travelling for both the cities
        return totalA + totalB
        