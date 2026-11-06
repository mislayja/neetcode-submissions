from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusts_list = [False]*n
        trusted_list = [0]*n

        # 2 pass...
        for truster, trusted in trust:
            trusted_list[trusted-1] +=1
            trusts_list[truster-1]=True
        
        # print(f"trusted_list={trusted_list}, trusts_list={trusts_list}")
        for idx in range(n):
            if trusted_list[idx]==(n-1) and trusts_list[idx]==False:
                return idx+1

        return -1