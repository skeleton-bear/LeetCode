# 很重要
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 这是一个拓扑问题,寻找是否有环
        # [ai, bi]可以看作一条有向边

        # 先构建邻接表
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        # 0: unvisited, 1: visiting, 2: visited
        visited = [0]* numCourses

        def dfs(course):
            # 如果状态为1说明在本次DFS中重复访问了这个点,代表图有环
            if visited[course] == 1:
                return False
            
            # 如果状态为2，说明这个节点是安全的，无需重复检查
            if visited[course] == 2:
                return True
            
            visited[course] = 1

            # 遍历所有的后继课程
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            
            # 探索完成标记为安全
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True





from collections import deque

class Solution:
    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        # 构建邻接表和入度数组
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # 将所有入度为0的课程入队
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0

        while queue:
            course = queue.popleft()
            courses_taken += 1

            # 遍历其后继课程，将其入度减1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                # 如果邻居的入度变为0，则入队
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return courses_taken == numCourses