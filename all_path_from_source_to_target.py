from collections import defaultdict,deque
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
        # def dfs(node,path):
        #     if node==(len(graph)-1):
        #         ans.append(path[:])

        #     for n in adjacency[node]:
        #         path.append(n)
        #         dfs(n,path)
        #         path.pop()
        # dfs(0,[0])
        # print(ans)
        # return ans

        # Iterative method
        #iterative method
        #The idea is to keep track of path when traversing to different node (it similar to dfs but faster)
        q = deque()
        q.append((0,[0]))
        while  q:
            node,path = q.popleft()
            if node==(len(graph)-1):
                ans.append(path)
            for n in adjacency[node]:
                q.append((n,path+[n]))
        
        return ans

    

