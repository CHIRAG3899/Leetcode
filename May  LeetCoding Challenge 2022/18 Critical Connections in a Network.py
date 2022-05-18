#There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
#
#A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
#
#Return all critical connections in the network in any order.
#
# 
#
#Example 1:
#
#
#Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
#Output: [[1,3]]
#Explanation: [[3,1]] is also accepted.
#Example 2:
#
#Input: n = 2, connections = [[0,1]]
#Output: [[0,1]]

class Solution(object):
    def __init__(self):
        self.timer = 0
		
    def criticalConnections(self, n, connections):
        low, timeV, visited = [0 for _ in range(n)], [0 for _ in range(n)], [False for _ in range(n)]
        graph = defaultdict(list)
        ans = []
        def tarjan(start, pre):
            visited[start] = True
            timeV[start] = low[start] = self.timer
            self.timer += 1
            for neighbor in graph[start]:
                if neighbor == pre: continue
                if visited[neighbor]:
                    low[start] = min(low[start], timeV[neighbor])
                else:
                    tarjan(neighbor, start)
                    low[start] = min(low[start], low[neighbor])
                    if low[neighbor] > timeV[start]:
                        ans.append([start, neighbor])        

            
        for i in range(len(connections)):
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])

        tarjan(0, -1)
        return ans
        
class Solution:
    def criticalConnections(self, n, connections):
        used, tin, fup = [0]*n, [-1]*n, [-1]*n
        self.timer, ans = 0, []
        graph = defaultdict(list)
        
        def dfs(node, par = -1):
            used[node] = 1
            tin[node] = fup[node] = self.timer + 1
            self.timer += 1
            for child in graph[node]:
                if child == par: continue
                if used[child] == 1:
                    fup[node] = min(fup[node], tin[child])
                else:
                    dfs(child, node)
                    fup[node] = min(fup[node], fup[child])
                    if fup[child] > tin[node]: ans.append([node, child])
        
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            
        for i in range(n):
            if not used[i]: dfs(i)
                
        return ans