class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # create dictionary for directed graph
        dic = defaultdict(list)
        for a, b in prerequisites:
            dic[b].append(a)
        print("dic:", dic)
        # use dfs to find cycle
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            indegrees[a] += 1
        
        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop()
            print("course:", course)
            for prereq in dic[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)
        return indegrees.count(0) == numCourses
