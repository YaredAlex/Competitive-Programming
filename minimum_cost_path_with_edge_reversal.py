"""
Docstring for minimum_cost_path_with_edge_reversal
"""
from collections import defaultdict,deque
import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # using dijkstra algorithm to expand best node
        # first extract neighbours
        adjecency_list = defaultdict(list)
        for edge in edges:
            inital_node = edge[0]
            terminal_node = edge[1]
            adjecency_list[inital_node].append((edge[2],edge[1]))
            adjecency_list[terminal_node].append((edge[2]*2,edge[0]))

        q =  [(0,0)] # initial edge
        costs = {0:0} # making first node "0" visited with cost "0"
        while q:
            cost,node = heapq.heappop(q)
            for e in adjecency_list[node]:
                n_cost,n_node = e
                if n_node not in costs or n_cost+cost<costs[n_node]:
                    costs[n_node] = n_cost+cost
                    heapq.heappush(q,(n_cost+cost,n_node))
        # print(costs)
        
        return costs.get(n-1,-1)


