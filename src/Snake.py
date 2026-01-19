class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
    
    def take_step(self, position):
        self.body.append(position)
        self.body.popleft()
    
    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

    def move(self):
        newHead = self.next_head()
        self.body.append(newHead)
        self.body.pop(0)
    
    def next_head(self):
        headRow, headCol = self.head()
        dirRow, dirCol = self.direction
        newHead = (headRow + dirRow, headCol + dirCol)
        return newHead
