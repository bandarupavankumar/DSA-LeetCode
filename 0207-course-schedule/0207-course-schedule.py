class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(course):
            if visited[course] == 1:  # found a cycle
                return False
            if visited[course] == 2:  # already checked
                return True
            
            visited[course] = 1  # mark as visiting
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            visited[course] = 2  # mark as visited
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True