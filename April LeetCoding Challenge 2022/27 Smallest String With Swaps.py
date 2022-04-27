#You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
#You can swap the characters at any pair of indices in the given pairs any number of times.
#
#Return the lexicographically smallest string that s can be changed to after using the swaps.
#
# 
#
#Example 1:
#
#Input: s = "dcab", pairs = [[0,3],[1,2]]
#Output: "bacd"
#Explaination: 
#Swap s[0] and s[3], s = "bcad"
#Swap s[1] and s[2], s = "bacd"
#Example 2:
#
#Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
#Output: "abcd"
#Explaination: 
#Swap s[0] and s[3], s = "bcad"
#Swap s[0] and s[2], s = "acbd"
#Swap s[1] and s[2], s = "abcd"
#Example 3:
#
#Input: s = "cba", pairs = [[0,1],[1,2]]
#Output: "abc"
#Explaination: 
#Swap s[0] and s[1], s = "bca"
#Swap s[1] and s[2], s = "bac"
#Swap s[0] and s[1], s = "abc"

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        G = [[] for _ in range(n)]
        for i,j in pairs:
            G[i].append(j)
            G[j].append(i)
        
        seen = [False]*n
        def dfs(i, indices):
            indices.append((i,s[i]))
            seen[i] = True
            for j in G[i]:
                if not seen[j]:
                    dfs(j, indices)

        ans = [None]*n
        for i in range(n):
            if not seen[i]:
                indices = []
                dfs(i, indices)
                if not indices:
                    ans[i] = s[i]
                else:
                    K = sorted(indices, key=lambda x:x[1])
                    P = sorted(indices, key=lambda x:x[0])
                    for i in range(len(indices)):
                        ans[P[i][0]] = K[i][1]
                        
        return "".join(ans)

