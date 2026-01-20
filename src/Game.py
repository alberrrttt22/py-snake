from src.Snake import Snake

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

INPUT_TO_DIR = {"w" : UP, "s" : DOWN, "a" : LEFT, "d" : RIGHT}

class Game:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(1,5), (2,5), (3,5), (4,5), (5,5), (6,5)], DOWN)
    
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

    def is_opposite(self, dir1, dir2):
        return dir1[0] == -dir2[0] and dir1[1] == -dir2[1]
    
    def hit_wall(self, next_pos):
        row, col = next_pos
        return row <= 0 or row >= self.height - 1 or col <= 0 or col >= self.width - 1
    
    def get_input(self):
        cmd = input("Enter an input (W/A/S/D and Enter): ").lower()
        return INPUT_TO_DIR.get(cmd, None)
    
    def render(self):
        print(self.board_matrix()) 
    
    def run(self):
        while True:
            self.render()
            tail = self.snake.body[0]
            cmd = self.get_input()

            if cmd and not self.is_opposite(cmd, self.snake.direction):
                self.snake.direction = cmd
    
            if self.hit_wall(self.snake.next_head()):
                print("Game Over. You hit a wall.")
                break
            if self.snake.next_head() in self.snake.body_set and self.snake.next_head() != tail:
                print("Game Over. You hit your own body.")
                break
            self.snake.move()

            

    

    

