class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = []

        for idx in range(len(matrix[0])):
            ret.append([])
            for inner_idx in range(len(matrix)):
                # we must access inner_idx
                ret[-1].append(matrix[inner_idx][idx])
                
            # this is idx where we need to 
        return ret