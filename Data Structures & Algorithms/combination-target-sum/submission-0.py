class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        res = []

        def recurse(candidates, target, soln):
            nonlocal res
            for idx, candidate in enumerate(candidates):
                # want to check if candidate+total > val, if so return early because candidates will always be sorted small to large
                if candidate > target: return

                # find and check all sums where we have repeated values and out target is >0 
                count = 1
                while (count*candidate) < target:
                    recurse(candidates[idx+1:], target-(count*candidate), soln + ([candidate]*count))
                    count+=1
                
                # last case, we need to add if our target == current sum
                if (count*candidate) == target:
                    # print(f"target={target}, candidate={candidate}, total={sum(soln)} count={count}, soln={soln}")
                    res.append(soln + ([candidate]*count))

        recurse(candidates, target, [])

        return res