from collections import defaultdict
import heapq
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # how to approch this problem
        adjecency = defaultdict(list)
        added = set()
        for i in range(len(original)):
            neighbor = changed[i]
            weight = cost[i]
            adjecency[original[i]].append((weight,neighbor))
            # key1 = original[i]+neighbor
            # if key1 not in added:
            #     adjecency[original[i]].append((weight,neighbor))
            #     added.add(key1)
        cache = {}
        def dijkstra(adjecency,start,end):
            q = [(0,start)]
            heapq.heapify(q)
            seen = {start:0}
            while q:
                weight,neighbor = heapq.heappop(q)
                for w,n in adjecency[neighbor]:
                    new_cost = weight+w
                    # if n==end:
                    #     print("found ",f" {n} == {end}")
                    #     return new_cost

                    if n not in seen or new_cost<seen[n]:
                        seen[n] = new_cost
                        heapq.heappush(q,(new_cost,n))
            cache[start] = seen
            # print(seen)
            return seen[end] if end in seen else -1
        ans = 0
        # print("adjecency ",adjecency)
        for i in range(len(source)):
            if source[i]==target[i]:
                continue
            if source[i] in cache:
                if target[i] in cache[source[i]]:
                    ans +=cache[source[i]][target[i]]
                else:
                    return -1
            # elif target[i] in cache:
            #     if source[i] in cache[target[i]]:
            #         ans +=cache[target[i]][source[i]]
            #     else:
            #         return -1
            else:
                best_cost = dijkstra(adjecency,source[i],target[i])
                if best_cost==-1:
                    return -1
                ans +=best_cost
        return ans

            