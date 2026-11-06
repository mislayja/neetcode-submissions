from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can iterate through prerequisites creating a hashmap from -> to for prerequisites
        # num:[num2, num3], ie to complete num we must complete num2, num3. 

        pre = {}
        for course, prereq in prerequisites:
            if course not in pre:
                pre[course]=list()
            pre[course].append(prereq)
        
        # ok we have a list of courses and the prereqs associated with them
        # do we just do dfs on this?  that seems wasteful
        # but I'm not sure how to do it better. 

        print(pre)

        def dfs(node, seen):
            # print(f"node={node}, seen={seen}, pre={pre}")
            if node in seen: return False
            # add it here
            if node in pre:
                seen.add(node)
                for prereq in pre[node]:
                    if not dfs(prereq, seen): return False
                seen.remove(node)
            return True
        
        for course in pre.keys():

            ret = dfs(course, set())
            # print(f"course={course} has prereqs{pre[course]}, with return value={ret}")
            # dfs call
            if not ret: return False

        return True
        