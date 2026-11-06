class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def exists( curr_pos, word, seen):
            # print(f"curr_pos={curr_pos}, word={word}, seen={seen}")
            if len(word)== 0: return True
            nonlocal board
            # need to iterate
            for delta_row, delta_col in ((-1,0),(1,0),(0,1),(0,-1)):
                next_row, next_col = delta_row+curr_pos[0], delta_col+curr_pos[1]
                # print(f"checking position={next_row},{next_col}")
                # out of bounds check
                if next_row <0 or next_row>= len(board) or next_col<0 or next_col>=len(board[0]): continue
                # print(f"in bounds :) position={next_row},{next_col} in bounds with char={board[next_row][next_col]}")
                # already used check
                if (next_row, next_col) in seen: continue

                # is valid check
                if board[next_row][next_col] == word[0]:
                    if exists((next_row, next_col), word[1:], seen+[(next_row, next_col)]): return True
            return False


        for row, l in enumerate(board):
            for col, char in enumerate(l):
                if char == word[0]:
                    # print(f"starting at pos, {row},{col}, with char={char}, remaining word:{word[1:]}")
                    # remaining_word = word[1:]
                    if exists((row,col), word[1:], [(row, col)]): return True
        
        return False