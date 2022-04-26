#You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
#The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
#Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
#
# 
#
#Example 1:
#
#
#Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#Output: 20
#Explanation: 
#
#We can connect the points as shown above to get the minimum cost of 20.
#Notice that there is a unique path between every pair of points.
#Example 2:
#
#Input: points = [[3,12],[-2,5],[-4,1]]
#Output: 18

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]
        
        # Track nodes which are included in MST.
        in_mst = [False] * n
        
        mst_cost = 0
        edges_used = 0
        
        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)
            
            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue
            
            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1
            
            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) +\
                                  abs(points[curr_node][1] - points[next_node][1])
                    
                    heapq.heappush(heap, (next_weight, next_node))
                    
        return mst_cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)  # obtain the current minimum edge
            res += d.pop((x, y))      # and remove the corresponding point
            for x1, y1 in d:          # for the rest of the points, update the minimum manhattan distance
                d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res