from src.Snake import Snake

UP = (1, 0)
DOWN = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Game:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(1,5), (2,5), (3,5), (4,5)], DOWN)
        self.board = self.board_matrix()
    
    def board_matrix(self):
        board = [[" " for i in range(self.width)] for j in range(self.height)]
        for col in range(self.width):
            board[0][col] = "#"
            board[self.height - 1][col] = "#"
        for row in range(1, self.height - 1):
            board[row][0] = "#"
            board[row][self.width - 1] = "#"
        for segment in self.snake.body:
            row, col = segment
            board[row][col] = "O"
        head_row, head_col = self.snake.head()
        board[head_row][head_col] = "X"
        board_strs = ["".join(row) for row in board]
        return "\n".join(board_strs)

    def render(self):
        
        print(self.board)
        # for row in matrix:
        #     print(row)
        # print("Height is " + str(self.height) + " and Width is " + str(self.width))
    

    

