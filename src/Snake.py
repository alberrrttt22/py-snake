class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.body_set = set(init_body)
    
    def take_step(self, position):
        self.body.append(position)
        self.body.popleft()
    
    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

    # need to remove tail first then add head, so that even when newHead == tail, we are making sure that the body_array perfectly matches body_set
    def move(self):
        tail = self.body[0]
        self.body.pop(0)
        self.body_set.remove(tail)
        # print("body array is : " + str(self.body))
        # print("body_set is : " + str(self.body_set))
        newHead = self.next_head()
        self.body.append(newHead)
        self.body_set.add(newHead)
    
    def next_head(self):
        headRow, headCol = self.head()
        dirRow, dirCol = self.direction
        newHead = (headRow + dirRow, headCol + dirCol)
        return newHead
