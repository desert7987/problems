from collections import deque

class MyQueue:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        element = self.dq.popleft()
        return element
        

    def peek(self) -> int:
        if self.dq:
            element = self.dq[0]
            return element
        

    def empty(self) -> bool:
        if self.dq:
            return False
        
        return True