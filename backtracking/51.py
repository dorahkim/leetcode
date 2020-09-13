# 51. N-Queens

class Solution:
    def backtracking(self, n: int, board: List[str]):
        # end point
        if n == self.n:
            self.rtn.append(copy.deepcopy(board))
            return
        
        # fill with dots
        for r in range(self.n):
            board[r] += '.'
        
        #add 'Q' in board[r][n]
        for r in range(self.n):
            
            # horizontal check
            if 'Q' in board[r]:
                continue
            
            # change '.' to 'Q'
            board[r] = board[r][:-1] + 'Q'
            
            # upper-left diagonal check
            tmpr = r - 1
            tmpc = n - 1
            flag = True
            while tmpr >= 0 and tmpc >= 0:
                if board[tmpr][tmpc] == 'Q':
                    flag = False
                    break
                tmpr -= 1
                tmpc -= 1
            
            if flag:
                # lower-left diagonal check
                tmpr = r + 1
                tmpc = n - 1
                while tmpr < self.n and tmpc >= 0:
                    if board[tmpr][tmpc] == 'Q':
                        flag = False
                        break
                    tmpr += 1
                    tmpc -= 1

                if flag:
                    # no eviction
                    self.backtracking(n + 1, board)
            
            # change 'A' back to '.'
            board[r] = board[r][:-1] + '.'
            
        for r in range(self.n):
            board[r] = board[r][:-1]
        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.rtn = []
        board = ['' for i in range(n)]
        self.backtracking(0, board)
        return self.rtn
