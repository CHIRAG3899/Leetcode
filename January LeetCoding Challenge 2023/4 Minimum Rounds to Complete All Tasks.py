# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

# Example 1:

# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
# Example 2:

# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
                                            # Example: tasks = [2,2,3,3,2,4,4,4,4,4,4,4]

        tasks = Counter(tasks)              #          tasks = {3:2, 2:3, 4:5}
        
        if 1 in tasks.values(): return -1   # <-- no solution if there's a singleton

        ans = 0                             # tasks.values() = [5, 3, 2]     
        for n in tasks.values():
            ans+= n//3 + bool(n%3)          # ans  = (3//3+False) + (2//3+True) + (4//3+True)
                                            #      = ( 1  +  0  ) + (  0 +  1 ) + (1   +  1 )
        return  ans                         #      = 4  <-- return
        
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c=0
        d={}
        tasks.sort()
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            while d[i]:
                if d[i]==1:
                    return -1
                if d[i]%3==0:
                    d[i]-=3
                else:
                    d[i]-=2
                c+=1
        return c

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)

        @cache
        def find(n):
            if n==2 or n==3:
                return 1

            if n<2:
                return inf

            return 1+min(
                find(n-2),
                find(n-3)
            )

        moves = 0
        for n in counts.values():
            move = find(n)

            if move==inf:
                return -1

            moves+=move

        return moves