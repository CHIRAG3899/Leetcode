#You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
#We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
#
# 
#
#Example 1:
#
#
#Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#Output: 2
#Example 2:
#
#Input: times = [[1,2,1]], n = 2, k = 1
#Output: 1
#Example 3:
#
#Input: times = [[1,2,1]], n = 2, k = 2
#Output: -1

class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1
        

class Solution:
    def networkDelayTime(self, times, N, K):
        t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1
        
class Solution(object):
#Dijkstra
    def networkDelayTime(self, times, N, K):
        adj_list = self.get_adj_list(times, N)
        heap = [(0, K)]
        distance_from_k = {}
        
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            distance_from_k[curr_node] = curr_dist
            if len(distance_from_k) == N:
                break
            for neighbor, weight in adj_list[curr_node]:
                if neighbor not in distance_from_k:
                    heapq.heappush(heap, (curr_dist + weight, neighbor))
                                       
        return max(distance_from_k.values()) if len(distance_from_k) == N else -1
        
    def get_adj_list(self, times, N):
        temp = {i:[] for i in range(1,N+1)}
        for node1, node2, weight in times:
            temp[node1].append((node2, weight))
        return temp

#Bellman Ford
class Solution(object):
    def networkDelayTime(self, times, N, K):
		# Initial Matrix Setup
        matrix = [[float('inf') for _ in range(N)] for _ in range(N)]
    
        for node1, node2, weight in times:
            matrix[node1-1][node2-1] = weight
        
        for i in range(len(matrix)):
            matrix[i][i] = 0 
         
		# Actual Iteration and Finding of Shortest Path
        for k in range(N):
            for node1 in range(N):
                for node2 in range(N):
                    matrix[node1][node2] = min(matrix[node1][node2], matrix[node1][k] + matrix[k][node2])
        
		return max(matrix[K-1]) if max(matrix[K-1]) != float('inf') else -1