from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # let's do dfs to traverse to all possible ways to reach n-1
        # backtracking is the way to do this
        
        # first let's build adjecancy
        adjacency = defaultdict(list)
        for i in range(len(graph)):
            adjacency[i].extend(graph[i])
        ans = []
        #recursive method
        def dfs(node,path):
            if node==(len(graph)-1):
                ans.append(path[:])

            for n in adjacency[node]:
                path.append(n)
                dfs(n,path)
                path.pop()
        dfs(0,[0])
        print(ans)
        return ans
    

